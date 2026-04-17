"""
Cotizador Automático de Autos - Tijuana
Ejecuta diariamente a las 6 PM hora de Tijuana
"""
import os
import time
import smtplib
import requests
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pytz
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PIL import Image
import base64
import io

# Configuración
EMAIL_USUARIO = "ajimenezdelara@gmail.com"
EMAIL_PASSWORD = "accc okcm xksc elpu"  
DESTINATARIO = "ajimenezdelara@gmail.com"

def obtener_fechas():
    """Obtiene fechas de pickup y return"""
    tz_tijuana = pytz.timezone('America/Tijuana')
    hoy = datetime.now(tz_tijuana)
    
    fecha_pickup = hoy + timedelta(days=2)  # 2 días después
    fecha_return = fecha_pickup + timedelta(days=1)  # 1 día de renta
    
    return {
        'pickup': fecha_pickup.strftime('%m/%d/%Y'),
        'return': fecha_return.strftime('%m/%d/%Y'),
        'pickup_display': fecha_pickup.strftime('%d/%m/%Y'),
        'return_display': fecha_return.strftime('%d/%m/%Y')
    }

def configurar_driver():
    """Configura el driver de Chrome para GitHub Actions"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome
