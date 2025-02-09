import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

arquivo_busca = "sua_busca_aqui.txt" # nome do arquivo que terá a lista de grupos encontrados
tempo_espera = 120 # entrar a cada 2 minutos = 120 segundos

service = Service()

options = Options()
options.add_argument("--headless") 
options.add_argument("--disable-gpu")
options.add_argument("--disable-notifications")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=service, options=options)

# Abra o site para carregar os cookies
driver.get("https://www.facebook.com/")

# Carregar os cookies salvos
with open("cookies.json", "r") as f:
    cookies = json.load(f)

# Adicionar os cookies ao navegador
for cookie in cookies:
    driver.add_cookie(cookie)

# Ler IDs dos grupos do arquivo
with open(arquivo_busca, "r") as arquivo:
    ids_grupos = [linha.strip() for linha in arquivo.readlines()]

# Criar lista de URLs dos grupos
urls_grupos = [f"https://www.facebook.com/groups/{group_id}" for group_id in ids_grupos]

# Percorrer cada grupo e tentar entrar
for url in urls_grupos:
    driver.get(url)  # Acessa a página do grupo
    time.sleep(3)  # Aguarda o carregamento da página

    entrou = False  # Variável para verificar se entrou no grupo

    # Buscar todos os elementos div e colocar dentro de uma lista
    lista_botoes = driver.find_elements(By.XPATH, "//div")
    for botao in lista_botoes:
        if botao.text == "Participar do grupo":
            botao.click()
            print(f"✅ Entrou no grupo: {url}")
            entrou = True  # Atualiza a variável para indicar sucesso
            time.sleep(tempo_espera - 3)  # Tempo de espera antes do próximo grupo
            break  # Sai do loop

    # Se não entrou, exibir mensagem de erro
    if not entrou:
        print(f"❌ Não foi possível entrar no grupo: {url}, pulando para o próximo...")

    time.sleep(3)  # Pequena pausa antes de carregar o próximo grupo
    continue

print("✅ Processo concluído!")
driver.quit()
