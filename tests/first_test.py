from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

def setup_driver():
    """Configura el driver de Chrome en modo headless"""
    options = Options()
    # Configurar opciones para evitar problemas de compatibilidad
    options.add_argument("--headless")  # Modo headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def test_google_search():
    """Test básico de búsqueda en Google"""
    driver = setup_driver()
    
    try:
        # Navegar a Google
        driver.get("https://www.google.com")
        
        # Esperar a que cargue la página
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        
        # Escribir en el buscador
        search_box.send_keys("Selenium Python")
        search_box.submit()
        
        # Esperar a que carguen los resultados
        time.sleep(2)
        
        # Verificar que hay resultados (más flexible)
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        assert len(results) > 0, "No se encontraron resultados de búsqueda"
        
        print("✅ Test de búsqueda en Google completado exitosamente")
        
    except Exception as e:
        print(f"❌ Error en el test: {e}")
        raise
    
    finally:
        driver.quit()

def test_page_title():
    """Test para verificar el título de una página"""
    driver = setup_driver()
    
    try:
        # Navegar a una página simple
        driver.get("https://www.python.org")
        
        # Verificar el título
        assert "Python" in driver.title
        assert driver.title == "Welcome to Python.org"
        
        print("✅ Test de título de página completado exitosamente")
        
    except Exception as e:
        print(f"❌ Error en el test: {e}")
        raise
    
    finally:
        driver.quit()

def test_simple_navigation():
    """Test simple de navegación"""
    driver = setup_driver()
    
    try:
        # Navegar a una página
        driver.get("https://httpbin.org/")
        
        # Verificar que la página cargó
        assert "httpbin" in driver.title.lower()
        
        # Verificar que hay contenido
        body = driver.find_element(By.TAG_NAME, "body")
        assert body.text != ""
        
        print("✅ Test de navegación simple completado exitosamente")
        
    except Exception as e:
        print(f"❌ Error en el test: {e}")
        raise
    
    finally:
        driver.quit()