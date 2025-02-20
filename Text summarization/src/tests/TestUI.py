from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir la página de Next.js
driver.get('http://localhost:3000')  # Asegúrate de que la URL sea correcta

try:
    # Esperar hasta que los botones sean visibles
    wait = WebDriverWait(driver, 10)
    
    # Encontrar todos los botones dentro de su contenedor usando la clase común del botón
    buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.grid button")))
    print(buttons)

    # Hacer clic en los botones uno por uno
    for i, button in enumerate(buttons):
        if i < 3:  # Solo los primeros tres botones (Transform, Summarize, Validate)
            button.click()
        
        # Encontrar el campo de texto y escribir
        text_area = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
        text_area.clear()
        
        if (i == 0):
            text_area.send_keys(f"Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all work together, and each person plays a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire questions at the actors to help them understand the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we work together to fix them.")
        elif (i == 1):
            text_area.send_keys(f"Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all work together, and each person plays a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire questions at the actors to help them understand the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we work together to fix them.")
        else:
            text_area.send_keys(f"The sun shines in the sky. Birds sing in the trees. John wakes up early every morning. He drinks his coffee and reads the newspaper. Then, he goes for a walk in the park. Flowers bloom and the air is fresh. Children play on the grass. Yesterday, John decided to visit his friend. He went to his house and they played music together. They ate pizza and laughed a lot. Afterward, they watched a movie. John felt happy to spend time with him.")


        # Hacer clic en el botón 'Submit'
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']")))
        submit_button.click()

finally:
    # Cerrar el navegador después de la prueba
    driver.quit()
