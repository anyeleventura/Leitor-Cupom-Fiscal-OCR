# Leitor de Cupom Fiscal com OCR e PDF

Este é um projeto de aplicação web que utiliza o poder da API Google Cloud Vision para realizar a Leitura Óptica de Caracteres (OCR) em imagens de cupons fiscais. A aplicação extrai informações importantes como dados da loja, lista de produtos, valores e totais, e apresenta os dados de forma organizada, permitindo ainda gerar um arquivo PDF com o resumo da compra.

O sistema permite o envio de imagens de duas formas:
1.  **Upload Local:** Selecionando um arquivo de imagem diretamente do computador.
2.  **Via Celular (QR Code):** Escaneando um QR Code para estabelecer uma conexão P2P (WebRTC) entre o celular e o computador, permitindo o envio da imagem sem a necessidade de cabos.

## ✨ Funcionalidades

-   **OCR de Alta Precisão:** Utiliza a API Google Vision para extrair texto de imagens.
-   **Parsing Inteligente:** Expressões regulares analisam o texto extraído para identificar e estruturar os dados do cupom.
-   **Interface Web Moderna:** Frontend limpo e responsivo para uma ótima experiência de usuário.
-   **Conexão via QR Code:** Envio de arquivos do celular para o desktop de forma simples e rápida com PeerJS.
-   **Geração de PDF:** Cria um relatório em PDF com os dados processados do cupom fiscal.

## 🛠️ Tecnologias Utilizadas

### **Backend**
-   **Python 3**
-   **Flask:** Micro-framework web para servir a aplicação.
-   **Google Cloud Vision API:** Para a funcionalidade de OCR.
-   **FPDF2:** Biblioteca para a criação de arquivos PDF.

### **Frontend**
-   **HTML5 / CSS3**
-   **JavaScript (Vanilla)**
-   **PeerJS:** Para a comunicação WebRTC (conexão via QR Code).
-   **QRCode.js:** Para gerar o QR Code na interface.

## 🚀 Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

### **Pré-requisitos**
-   Python 3.8 ou superior
-   Conta no Google Cloud Platform com a API Cloud Vision ativada.

### **Passos**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/Leitor-Cupom-Fiscal-OCR.git](https://github.com/SEU-USUARIO/Leitor-Cupom-Fiscal-OCR.git)
    cd Leitor-Cupom-Fiscal-OCR
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as credenciais do Google Cloud:**
    -   Crie uma chave de conta de serviço no seu projeto do Google Cloud Platform e baixe o arquivo JSON.
    -   Renomeie o arquivo para `credentials.json` e coloque-o na raiz do projeto.
    -   **Importante:** Este arquivo é sensível. Ele já está incluído no `.gitignore` para não ser enviado ao seu repositório público.

5.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    - A aplicação estará disponível em `http://127.0.0.1:8000` ou no IP da sua máquina na rede local (ex: `http://192.168.18.22:8000`).

## 📝 Pontos de Melhoria

-   **IP Hardcoded:** O endereço `http://192.168.18.22:8000` está fixo no JavaScript para a geração do QR Code. O ideal é obter o endereço dinamicamente (`window.location.host`) para que funcione em qualquer rede sem alterações no código.
-   **Melhorar as Expressões Regulares (Regex):** Os padrões de regex podem ser aprimorados para suportar uma variedade maior de layouts de cupons fiscais.
-   **Contenerização com Docker:** Adicionar um `Dockerfile` para facilitar o deploy e a execução do ambiente.