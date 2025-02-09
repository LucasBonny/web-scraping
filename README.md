# Facebook id groups scraper

A intenção é pegar os ids de todos os grupos de uma busca no Facebook.

## Requisitos

- Python 3
- Selenium


### Instalar o Selenium
```bash
pip install selenium webdriver-manager
```

## Como usar

Para usar deverá fazer login no Facebook inserindo seu email e senha no arquivo `login_facebook.py`.

```python
driver.find_element(By.ID, "email").send_keys("seu email") # linha 17
driver.find_element(By.ID, "pass").send_keys("sua senha", Keys.RETURN) # linha 18
```
para garantir o bom funcionamento irá aparecer um navegador para dar continuidade no login quando executar o arquivo `login_facebook.py`.

```bash
python ./login_facebook.py
```
Ao efetuar o login irá gerar um cookie para que as buscas possam ser efetuadas corretamente.

E com isso, altere a informação de busca no arquivo `busca_facebook.py`.

```python
busca = "sua busca" # linha 9
```
Após isso, basta executar o comando na raiz do projeto, e a busca irá ser realizada.

```bash
python ./busca_facebook.py
```

Agora é só esperar a busca terminar e o resultado estará disponível no arquivo `busca_sua_busca.txt`.

### Entrar nos grupos

Se por acaso queira entrar nos grupos do facebook, basta alterar as linhas 9 e 10

```py
arquivo_busca = "sua_busca_aqui.txt" # nome do arquivo que terá a lista de grupos encontrados
tempo_espera = 120 # entrar a cada 2 minutos = 120 segundos
```

Para executar iniciar, basta usar o comando abaixo:

```bash
python .\entrar_grupo_facebook.py
```