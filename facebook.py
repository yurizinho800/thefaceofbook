logo = """  
                 ████████████████████
                ██████████████████████
               █████████████████████████
              ████████████        ███████
              ███████████         ███████
             ████████████     ████████████
             ████████████     ████████████
             ████████             ████████
             █████████           █████████
              ███████████     ███████████
              ███████████     ██████████
               ██████████     █████████
                ██████████████████████
                 ████████████████████


"""

from colorama import Fore, Back, Style
print(Fore.BLUE + Style.BRIGHT + Back.WHITE + logo + Fore.RESET)

import getpass
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys


username = input(Fore.RED + "Digite o seu login do usuario: ")
password = getpass.getpass("Agora a palavra chave: ")
service = Service(executable_path='/home/blackhat/chromedriver/linux-116.0.5793.0/chromedriver/linux-125.0.6422.60/chromedriver-linux64/chromedriver')

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
# Abre a página da web
url = 'https://www.facebook.com/'
driver.get(url)

# Localiza o elemento que contém as informações dos amigos (use inspecionar elemento no navegador para encontrar o seletor correto)
# Suponha que o <iframe> tenha o atributo "name" ou "id" igual a "meu_iframe"
driver.implicitly_wait(50)

campo_usuario = driver.find_element(By.ID, "email")

campo_senha = driver.find_element(By.ID, "pass")

campo_usuario.send_keys(username)

campo_senha.send_keys(password)

botao = driver.find_element(By.CLASS_NAME, "selected")

botao.click()
print("login bem-sucedido!")

time.sleep(9900)
#  print("Falha no login")
quit()
