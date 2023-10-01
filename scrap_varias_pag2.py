
from selenium.webdriver.support import expected_conditions
from seleniumbase import Driver
from selenium.webdriver.support.wait import WebDriverWait
from a_selenium2df import get_df
from selenium.webdriver.common.by import By
import pandas as pd
from PrettyColorPrinter import add_printer

add_printer(1)

drivers = {}
nomes = [
    "https://www.google.com",
    "https://www.uol.com.br",
    
]

# criando os objetos Driver para cada site
for nome in nomes:
    drivers[nome] = Driver(uc=True)

# carregando os sites em threads separadas
import threading
def abrir_site(nome):
    drivers[nome].get(nome) # usando a variável nome para acessar o dicionário drivers

for nome in nomes:
    try:
        threading.Thread(target=abrir_site, args=(nome,)).start()
    except Exception as e:
        print(e)
        continue

# implementar ações
def g(driver, q="a",): # adicionando o parâmetro driver e mudando o valor padrão de q para "a"
    return get_df(driver, By, WebDriverWait, expected_conditions, queryselector=q, with_methods=True, )

resultados = []

def fazer_acoes(nome):
    driver = drivers[nome] # obtendo o objeto Driver correspondente ao nome do site
    df = g(driver) # passando o objeto Driver para a função g
    print(df)
    resultados.append(df)

for nome in nomes:
    try:
        threading.Thread(target=fazer_acoes, args=(nome,)).start()
    except Exception as e:
        print(e)
        continue
