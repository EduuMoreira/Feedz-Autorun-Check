from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Informa o navegador usado - linha 7
navegador = webdriver.Chrome()

# Aqui da entrada na URL usada - linha 10
navegador.get("https://app.feedz.com.br/inicio")

# Aqui da um tempo para o JS carregar - linha 13
time.sleep(3)

# Aqui da entrada para preenchimento do campo usurário - linha 16
username = navegador.find_element_by_id("login_email").send_keys("COLOQUE O SEU EMAIL AQUI")

# Aqui da entrada para preenchimento do campo senha - linha 19
password = navegador.find_element_by_xpath('//*[@id="formLogin"]/div[2]/div/div/input').send_keys("COLOQUE A SUA SENHA AQUI")

# Aqui entra após os campos preenchidos - linha 22
enter = navegador.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/form/div[3]/button').click()

# Aqui da um tempo para o JS carregar - linha 25
time.sleep(5)

# Aqui clica na carinha do termometro de humor - linha 28
humor_face = navegador.find_element_by_xpath('//*[@id="fdz-panel-form-mood"]/div[1]/div/label[5]/img').click()

# Aqui clica em enviar a seleção - linha 31
navegador.find_element_by_xpath('//*[@id="fdz-panel-form-mood"]/div[2]/div/button[2]').click()

# Tempo para o JS Carregar - Linha 34
time.sleep(3)

# Aqui fecha o navegador após a execução - Linha 37
navegador.close()

# Usa o comando no terminal para gerar as pastas - pyinstaller app.py