from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def explore_google_elements():
    """Explora diferentes formas de encontrar elementos en Google"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    
    try:
        browser.get("https://www.google.com")
        time.sleep(2)
        
        print("🔍 Explorando elementos en Google.com")
        print("=" * 50)
        
        # 1. Buscar por ID
        print("\n📋 Elementos por ID:")
        elements_with_id = browser.find_elements(By.CSS_SELECTOR, "[id]")
        for element in elements_with_id[:5]:  # Mostrar solo los primeros 5
            element_id = element.get_attribute("id")
            print(f"   ID: '{element_id}'")
        
        # 2. Buscar por NAME (más común en formularios)
        print("\n📋 Elementos por NAME:")
        elements_with_name = browser.find_elements(By.CSS_SELECTOR, "[name]")
        for element in elements_with_name:
            name = element.get_attribute("name")
            tag = element.tag_name
            print(f"   NAME: '{name}' | TAG: {tag}")
        
        # 3. Buscar por CLASS
        print("\n📋 Algunas clases CSS:")
        elements_with_class = browser.find_elements(By.CSS_SELECTOR, "[class]")
        classes_found = set()
        for element in elements_with_class[:10]:
            class_name = element.get_attribute("class")
            if class_name:
                classes_found.add(class_name)
        
        for class_name in list(classes_found)[:5]:
            print(f"   CLASS: '{class_name}'")
        
        # 4. Buscar elementos específicos
        print("\n📋 Elementos específicos:")
        
        # Campo de búsqueda
        try:
            search_box = browser.find_element(By.NAME, "q")
            print(f"   ✅ Campo de búsqueda encontrado: {search_box.tag_name}")
        except:
            print("   ❌ Campo de búsqueda no encontrado")
        
        # Botón de búsqueda
        try:
            search_button = browser.find_element(By.NAME, "btnK")
            print(f"   ✅ Botón de búsqueda encontrado: {search_button.tag_name}")
        except:
            print("   ❌ Botón de búsqueda no encontrado")
        
        # Logo de Google
        try:
            logo = browser.find_element(By.ID, "hplogo")
            print(f"   ✅ Logo encontrado: {logo.tag_name}")
        except:
            print("   ❌ Logo no encontrado")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        browser.quit()

if __name__ == "__main__":
    explore_google_elements() 