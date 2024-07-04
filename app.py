import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

#carregar as credenciais do arquivo config.json
with open('config.json') as config_file:
    config = json.load(config_file)

login = config['username']
senha = config['password']

#configurar o webdriver 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    #acessar site 
    driver.get('http://the-internet.herokuapp.com/login')

    campo_usuario = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    campo_usuario.send_keys(login)

    campo_senha = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )

    campo_senha.send_keys(senha)

    btn_submit = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]'))
    )

    btn_submit.click()

finally:
    time.sleep(5)
    print('Fim do programa')
