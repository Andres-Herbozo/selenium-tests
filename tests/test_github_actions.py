import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    """Fixture para crear el driver de Chrome configurado para CI/CD"""
    options = Options()
    
    # Configuración específica para GitHub Actions
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    
    driver.quit()

@pytest.mark.selenium
@pytest.mark.headless
def test_google_page_load(driver):
    """Test básico de carga de página de Google"""
    driver.get("https://www.google.com")
    
    # Verificar que la página cargó
    assert "Google" in driver.title
    
    # Verificar que el campo de búsqueda está presente
    search_box = driver.find_element(By.NAME, "q")
    assert search_box.is_displayed()

@pytest.mark.selenium
@pytest.mark.headless
def test_python_org_page(driver):
    """Test de la página de Python.org"""
    driver.get("https://www.python.org")
    
    # Verificar título
    assert "Python" in driver.title
    assert driver.title == "Welcome to Python.org"
    
    # Verificar que hay contenido
    body = driver.find_element(By.TAG_NAME, "body")
    assert body.text != ""

@pytest.mark.selenium
@pytest.mark.headless
@pytest.mark.slow
def test_multiple_sites(driver):
    """Test navegando por múltiples sitios"""
    sites = [
        ("https://httpbin.org/", "httpbin"),
        ("https://www.github.com", "GitHub"),
    ]
    
    for url, expected_text in sites:
        driver.get(url)
        assert expected_text in driver.title
        print(f"✅ {expected_text} cargado correctamente")

@pytest.mark.selenium
@pytest.mark.headless
def test_element_interaction(driver):
    """Test de interacción con elementos"""
    driver.get("https://www.google.com")
    
    # Encontrar campo de búsqueda
    search_box = driver.find_element(By.NAME, "q")
    
    # Escribir texto
    search_box.send_keys("Selenium Python")
    
    # Verificar que el texto se escribió
    assert search_box.get_attribute("value") == "Selenium Python" 