import os
from flask import Flask, render_template, request, jsonify, make_response
from google.cloud import vision
from dotenv import load_dotenv
from fpdf import FPDF

# Carrega as variáveis de ambiente
load_dotenv()

# Define o caminho para o arquivo de credenciais
# É importante que o arquivo 'credentials.json' esteja na mesma pasta
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

app = Flask(__name__)

# Instancia o cliente da Google Vision API
vision_client = vision.ImageAnnotatorClient()

# Classe customizada para criar o PDF com cabeçalho e rodapé
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Cupom Fiscal Processado', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
        
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(2)

    def chapter_body(self, data):
        self.set_font('Arial', '', 11)
        for key, value in data.items():
            self.multi_cell(0, 6, f'{key}: {value}')
        self.ln(5)
        
    def products_table(self, header, data):
        self.set_font('Arial', 'B', 8)
        # Larguras das colunas (ajustadas para caber)
        col_widths = [20, 70, 15, 15, 25, 25] 
        for i, header_text in enumerate(header):
            self.cell(col_widths[i], 7, header_text, 1, 0, 'C')
        self.ln()
        
        self.set_font('Arial', '', 8)
        for row in data:
            self.cell(col_widths[0], 6, row['code'], 1)
            self.cell(col_widths[1], 6, row['description'][:45], 1) # Limita a descrição
            self.cell(col_widths[2], 6, str(row['quantity']), 1, 0, 'C')
            self.cell(col_widths[3], 6, row['unit'], 1, 0, 'C')
            self.cell(col_widths[4], 6, f"R$ {row['unitValue']}", 1, 0, 'R')
            self.cell(col_widths[5], 6, f"R$ {row['itemValue']}", 1, 0, 'R')
            self.ln()
            
        # Linha de total
        self.set_font('Arial', 'B', 9)
        self.cell(sum(col_widths[:-1]), 7, 'TOTAL', 1, 0, 'R')
        self.cell(col_widths[-1], 7, f"R$ {request.get_json().get('totalValue', '0,00')}", 1, 0, 'R')
        self.ln()


@app.route('/')
def index():
    """Serve a página principal (nosso index.html)."""
    return render_template('index.html')

@app.route('/process-image', methods=['POST'])
def process_image():
    """Recebe a imagem, envia para a Google Vision e retorna o texto."""
    
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    content = file.read()
    image = vision.Image(content=content)
    
    response = vision_client.text_detection(image=image)
    texts = response.text_annotations
    
    if response.error.message:
        return jsonify({'error': f'Google Vision API Error: {response.error.message}'}), 500

    if texts:
        full_text = texts[0].description
        return jsonify({'text': full_text})
    else:
        return jsonify({'text': ''})

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    """Recebe os dados do cupom em JSON e gera um PDF."""
    data = request.get_json()
    
    pdf = PDF()
    pdf.add_page()
    
    # Adiciona informações da loja
    store_info = data.get('storeInfo', {})
    pdf.chapter_title('Empresa Vendedora')
    pdf.chapter_body({
        'Nome': store_info.get('name', '-'),
        'CNPJ': store_info.get('cnpj', '-'),
        'Endereço': store_info.get('address', '-')
    })
    
    # Adiciona a tabela de produtos
    products = data.get('products', [])
    if products:
        pdf.chapter_title('Produtos')
        table_header = ['Código', 'Descrição', 'Qtd.', 'UN', 'Vl. Unit.', 'Vl. Item R$']
        pdf.products_table(table_header, products)
    
    pdf.ln(10) # Espaçamento
    
    # Adiciona resumo da venda e informações de pagamento
    sale_info = data.get('saleInfo', {})
    payment_info = data.get('paymentInfo', {})
    pdf.chapter_title('Resumo da Venda e Pagamento')
    pdf.chapter_body({
        'Qtd. total de itens': str(sale_info.get('totalItems', '-')),
        'Valor total': f"R$ {data.get('totalValue', '0,00')}",
        'Operador': sale_info.get('operator', '-'),
        'Tipo de Pagamento': payment_info.get('type', '-'),
        'Troco': f"R$ {payment_info.get('change', '0,00')}"
    })

    # Gera o PDF em memória
    pdf_output = pdf.output(dest='S').encode('latin-1')
    
    # Cria uma resposta Flask para enviar o arquivo
    response = make_response(pdf_output)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=cupom_fiscal.pdf'
    
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)