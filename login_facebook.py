import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service()

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.facebook.com/")

driver.find_element(By.ID, "email").send_keys("seu email")
driver.find_element(By.ID, "pass").send_keys("sua senha", Keys.RETURN)

while True:
    if driver.current_url.startswith("https://www.facebook.com/two_factor/remember_browser/"):
        print("Usuário está na autenticação de 2 fatores, só aguardar!")
        time.sleep(2)
        # procurar o botão div e clicar
        driver.find_element(By.XPATH, "(//div)[70]").click()
        
    if driver.current_url == "https://www.facebook.com/":
        print("Usuário foi redirecionado para a página inicial do Facebook!")
        break  # Sai do loop quando a página inicial for detectada

# Salvar os cookies após o login
cookies = driver.get_cookies()

# Salve os cookies em um arquivo JSON
with open("cookies.json", "w") as f:
    json.dump(cookies, f)

print("Cookies salvos com sucesso!")
driver.quit()