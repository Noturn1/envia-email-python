# Envia Email com Anexo

Este projeto é um script Python que envia um e-mail com um arquivo anexado usando o servidor SMTP do Gmail. O usuário pode fornecer o caminho do arquivo e o e-mail do destinatário diretamente no terminal.

## Pré-requisitos

- Python 3.x
- Conta no Gmail
- Permitir "Acesso a apps menos seguros" na sua conta do Gmail (Recomendado criar uma senha de aplicativo no google)

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/Noturn1/envia-email-python.git
    cd seu-repositorio
    ```

2. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração

1. Defina as variáveis de ambiente `SENDER_EMAIL` e `SENDER_PASSWORD` com suas credenciais do Gmail:
    ```sh
    export SENDER_EMAIL="seu_email@gmail.com"
    export SENDER_PASSWORD="sua_senha"
    ```

## Uso

1. Execute o script:
    ```sh
    python3 envia-email.py
    ```

2. Quando solicitado, insira o caminho do arquivo que deseja enviar e o e-mail do destinatário.

## Exemplo

```sh
$ python3 envia-email.py
Digite o caminho do arquivo: /caminho/para/seu/arquivo/documento.docx
Digite o e-mail do destinatário: destinatario@example.com
