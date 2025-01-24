from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

def send_email(file: str, email: str):
    try:
        # Configurações do servidor SMTP
        SMTP_SERVER = "smtp.gmail.com"
        SMTP_PORT = 587
        SENDER_EMAIL = os.getenv("SENDER_EMAIL")  
        SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  

        if not SENDER_EMAIL or not SENDER_PASSWORD:
            raise ValueError("E-mail ou senha do remetente não configurados nas variáveis de ambiente.")

        # Verificar se o arquivo existe
        if not os.path.exists(file):
            raise FileNotFoundError(f"Arquivo '{file}' não encontrado.")

        # Criando a mensagem de e-mail
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = email
        msg['Subject'] = "Envio de arquivo .docx"
        msg['Date'] = formatdate(localtime=True)

        # Corpo do e-mail
        body = "Segue em anexo o arquivo solicitado."
        msg.attach(MIMEText(body, 'plain'))

        # Anexando o arquivo
        with open(file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {os.path.basename(file)}",
            )
            msg.attach(part)

        # Enviando o e-mail
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
        
        logging.info("E-mail enviado com sucesso.")

    except Exception as e:
        logging.error(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    file_path = input("Digite o caminho do arquivo: ")
    recipient_email = input("Digite o e-mail do destinatário: ")
    send_email(file_path, recipient_email)