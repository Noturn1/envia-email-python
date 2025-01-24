import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(file: str, email: str) :
    # Configurações do servidor SMTP
    SMTP_SERVER = "smtp.gmail.com"  
    SMTP_PORT = 587
    SENDER_EMAIL = 
    SENDER_PASSWORD = 
    
    # Verificar se o arquivo existe
    if not os.path.exists(file):
        raise FileNotFoundError(f"Arquivo '{file}' não encontrado.")

    # Criando a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = email
    msg['Subject'] = "Envio de arquivo .docx" 

    # Corpo do e-mail
    body = "Segue em anexo o arquivo solicitado."
    msg.attach(MIMEText(body, 'plain'))

    # Anexando o arquivo
    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file)}")
        msg.attach(part)

    # Enviando o e-mail
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, email, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso para:", email)
    except smtplib.SMTPException as e:
        print("Falha ao enviar o e-mail:", e)

if __name__ == "__main__":
    file_path = "documentos.docx"
    recipient_email = "destinatario@example.com"
    send_email(file_path, recipient_email)