from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_page_title():
    """Test corregido para verificar el título de Google"""
    # Configurar opciones para evitar problemas de compatibilidad
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Usar webdriver_manager para gestionar el driver automáticamente
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
    try:
        # Navegar a Google
        browser.get("https://www.google.com")
        
        # Verificar que estamos en Google (más realista)
        assert "Google" in browser.title
        
        # Buscar el campo de búsqueda (elemento que sí existe en Google)
        search_box = browser.find_element(By.NAME, "q")
        assert search_box.is_displayed()
        
        print("✅ Test de Google completado exitosamente")
        
    except Exception as e:
        print(f"❌ Error en el test: {e}")
        raise
    
    finally:
        browser.quit() 