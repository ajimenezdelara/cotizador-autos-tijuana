import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import pytz

def test_email():
    """Prueba básica de envío de email"""
    try:
        print("Iniciando prueba de email...")
        
        # Obtener credenciales
        email_usuario = os.getenv('EMAIL_USUARIO')
        email_password = os.getenv('EMAIL_PASSWORD')
        
        if not email_usuario or not email_password:
            print("ERROR: Faltan variables de entorno EMAIL_USUARIO o EMAIL_PASSWORD")
            return False
            
        print(f"Email usuario: {email_usuario}")
        print("Password configurado: Sí" if email_password else "No")
        
        # Crear mensaje
        msg = MIMEMultipart()
        msg['From'] = email_usuario
        msg['To'] = "armando.jimenez@avis.com.mx"
        msg['Subject'] = "Prueba de Script - Cotizador"
        
        tijuana_tz = pytz.timezone('America/Tijuana')
        fecha_actual = datetime.now(tijuana_tz).strftime("%d/%m/%Y %H:%M")
        
        cuerpo = f"""
        Prueba del script cotizador
        Fecha de ejecución: {fecha_actual}
        
        Este es un email de prueba para verificar que el sistema funciona correctamente.
        """
        
        msg.attach(MIMEText(cuerpo, 'plain'))
        
        # Enviar email
        print("Conectando a Gmail...")
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(email_usuario, email_password)
        servidor.send_message(msg)
        servidor.quit()
        
        print("✅ Email de prueba enviado correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error enviando email: {e}")
        return False

if __name__ == "__main__":
    print("=== SCRIPT DE PRUEBA COTIZADOR ===")
    test_email()
