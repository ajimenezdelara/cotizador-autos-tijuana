import time
import os
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pytz

def configurar_driver():
    """Configura el driver de Chrome para GitHub Actions"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-plugins")
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def obtener_fecha_consulta():
    """Obtiene la fecha de consulta (2 días después de hoy) en timezone de Tijuana"""
    tijuana_tz = pytz.timezone('America/Tijuana')
    fecha_actual = datetime.now(tijuana_tz)
    fecha_consulta = fecha_actual + timedelta(days=2)
    return fecha_consulta.strftime("%Y-%m-%d")

def cotizar_mexrentacar(driver):
    """Cotiza en MexRentaCar"""
    try:
        print("Cotizando en MexRentaCar...")
        driver.get("https://mexrentacar.com/")
        
        # Esperar a que cargue la página
        WebDriverWait(driver, 10).wait(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        time.sleep(3)
        screenshot_path = "mexrentacar_screenshot.png"
        driver.save_screenshot(screenshot_path)
        print("Captura de MexRentaCar guardada")
        return screenshot_path
        
    except Exception as e:
        print(f"Error en MexRentaCar: {e}")
        return None

def cotizar_hertz(driver):
    """Cotiza en Hertz México"""
    try:
        print("Cotizando en Hertz...")
        driver.get("https://www.hertzmexico.com/")
        
        # Esperar a que cargue la página
        WebDriverWait(driver, 10).wait(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        time.sleep(3)
        screenshot_path = "hertz_screenshot.png"
        driver.save_screenshot(screenshot_path)
        print("Captura de Hertz guardada")
        return screenshot_path
        
    except Exception as e:
        print(f"Error en Hertz: {e}")
        return None

def cotizar_optima(driver):
    """Cotiza en Optima RentaCar"""
    try:
        print("Cotizando en Optima...")
        driver.get("https://optimarentacar.com.mx/")
        
        # Esperar a que cargue la página
        WebDriverWait(driver, 10).wait(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        time.sleep(3)
        screenshot_path = "optima_screenshot.png"
        driver.save_screenshot(screenshot_path)
        print("Captura de Optima guardada")
