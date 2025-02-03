import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import datetime

busca = "sua busca"

service = Service()

options = Options()
options.add_argument("--headless") 
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=service, options=options)

data_hoje = datetime.datetime.now().strftime("%Y-%m-%d")

# Abra o site para carregar os cookies
driver.get("https://www.facebook.com/")

# Carregar os cookies salvos
with open("cookies.json", "r") as f:
    cookies = json.load(f)

# Adicionar os cookies ao navegador
for cookie in cookies:
    driver.add_cookie(cookie)

busca = "?q=" + busca
busca = busca.replace(" ", "%20")
driver.get("https://www.facebook.com/search/groups/" + busca)

qnt = 23
busca = busca.replace("?q=", "")
busca = busca.replace("%20", "_")
nome_arquivo = f"busca_{busca}.txt"
scroll_count = 0

while True:
    try:
        # Pausa para dar tempo para a página carregar
        time.sleep(0.5)
        
        # Captura o link
        url = driver.find_elements(By.TAG_NAME, 'a')[qnt].get_attribute('href')
        partes = url.split('/')
        print(url)
        
        # Grava o link no arquivo
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write(partes[4] + "\n")
    
        qnt += 2

        # Rola a página a cada link capturado
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Aguarda um pouco para garantir que a página carregue os próximos resultados
        time.sleep(0.5)
        
    except IndexError:
        # Se atingir o fim dos links disponíveis na página, para o loop
        print("Fim dos links de" + busca + " encontrados!")
        break

print(f"Arquivo '{nome_arquivo}' criado e dados gravados com sucesso!")
