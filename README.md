# 🧾 Leitor de Cupom Fiscal com OCR e PDF

Este projeto é uma aplicação web completa que utiliza o poder da API **Google Cloud Vision** para realizar a Leitura Óptica de Caracteres (OCR) em imagens de cupons fiscais. A aplicação extrai informações cruciais como dados da loja, lista de produtos, valores e totais, e apresenta os dados de forma organizada, permitindo ainda gerar um arquivo **PDF** com o resumo da compra.

O sistema foi desenhado com flexibilidade, permitindo o envio de imagens de duas formas intuitivas:

1.  **Upload Local:** Selecionando um arquivo de imagem diretamente do computador.
2.  **Via Celular (QR Code):** Escaneando um QR Code para estabelecer uma conexão P2P (via WebRTC) entre o celular e o computador, permitindo o envio da imagem de forma prática e sem a necessidade de cabos.

## ✨ Funcionalidades Principais

  - **OCR de Alta Precisão:** Utiliza a **API Google Vision** para extrair texto de imagens de forma rápida e confiável.
  - **Parsing Inteligente de Dados:** Expressões regulares robustas analisam o texto extraído para identificar, formatar e estruturar os dados do cupom (loja, CNPJ, produtos, totais, etc.).
  - **Interface Web Moderna:** Frontend limpo, responsivo e intuitivo para uma ótima experiência de usuário em qualquer dispositivo.
  - **Conexão Dinâmica via QR Code:** Gera um QR Code com o endereço de rede local da aplicação, permitindo o envio de arquivos do celular para o desktop de forma simples com **PeerJS**, sem necessidade de configuração manual de IP.
  - **Geração de PDF:** Cria um relatório em PDF bem formatado com os dados processados do cupom fiscal, pronto para ser salvo ou impresso.

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Backend** | 🐍 **Python 3** | Linguagem principal da aplicação. |
| | Flask | Micro-framework web para servir a aplicação e as APIs. |
| | Google Cloud Vision | Serviço de OCR para extração de texto das imagens. |
| | FPDF2 | Biblioteca para a criação programática de arquivos PDF. |
| **Frontend**| 🌐 **HTML5 / CSS3** | Estrutura e estilo da página. |
| | 🍦 **JavaScript (Vanilla)** | Lógica de interação, manipulação do DOM e comunicação. |
| | PeerJS | Implementação da comunicação WebRTC para a conexão P2P. |
| | QRCode.js | Geração do QR Code dinâmico na interface. |

## 🚀 Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

  - **Python 3.8** ou superior.
  - Conta no **Google Cloud Platform** com a **API Cloud Vision** ativada.

### Passos

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/SEU-USUARIO/Leitor-Cupom-Fiscal-OCR.git
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

3.  **Instale as dependências do Python:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as credenciais do Google Cloud:**

      - No seu projeto do Google Cloud, crie uma **chave de conta de serviço** para a API Vision e baixe o arquivo de credenciais **JSON**.
      - Renomeie este arquivo para `credentials.json` e coloque-o na pasta raiz do projeto.
      - **Importante:** Este arquivo é sensível. Ele já está incluído no `.gitignore` para não ser enviado acidentalmente ao seu repositório público.

5.  **Execute a aplicação:**

    ```bash
    python app.py
    ```

      - O servidor Flask será iniciado. Acesse a aplicação no seu navegador através do endereço fornecido no terminal (geralmente `http://127.0.0.1:8000` para testes locais, ou um IP de rede como `http://192.168.1.10:8000` para acesso de outros dispositivos).

## 👨‍💻 Como Usar

### Opção 1: Upload de Arquivo Local

1.  Clique no botão **"Adicionar por arquivo local"**.
2.  Selecione uma imagem (`.jpg`, `.png`, etc.) de um cupom fiscal.
3.  Aguarde o processamento. Os dados extraídos aparecerão na tela.
4.  Clique em **"Gerar PDF"** para baixar o relatório.

### Opção 2: Envio via Celular (QR Code)

1.  Clique em **"Adicionar por celular (QR Code)"**. Um QR Code será exibido.
2.  Abra a câmera do seu celular e escaneie o QR Code. Isso abrirá uma página no navegador do seu celular.
3.  Na página do celular, clique em **"Selecionar Arquivo"** e escolha a foto do cupom fiscal.
4.  O arquivo será enviado para o computador via P2P. Os dados processados aparecerão automaticamente na tela do computador.
5.  Clique em **"Gerar PDF"** no computador para baixar o relatório.
