# A primeira etapa foi importar as bibliotecas necessárias para webscraping. Por ser um site que requer dinâmicas específicas
# para carregar o html que contém dados das vagas, utilizei o selenium para abrir a url, pesquisar um termo de preferência, 
# descer a página n vezes e coletar os dados carregados.

import requests
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = "https://portal.gupy.io/"

# Insere a opção de não abrir o driver enquanto ocorre o scraping.
options = Options()
options.add_argument("--headless=new")

# Utiliza o webdriver do Chrome para abrir a url.
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

sleep(1)

# Coloca no menu de pesquisar a palavra estágio, clica no botão e acessa os resultados.
input_place = driver.find_element(By.TAG_NAME, 'input').send_keys('estágio')
click_place = driver.find_element(By.XPATH, "/html/body/div/main/div/div/div[2]/div/div/div/div/div[2]/button")
click_place.click()
sleep(3)

# Cria uma função para scrollar a página até o final infinitas vezes, parando somente 
# quando todos os resultados forem carregados.

def scrolling_page():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    sleep(1)  
    
while True:
    prev_height = driver.execute_script("return document.body.scrollHeight")
    scrolling_page()
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == prev_height:
        break

# Carrega o html do driver utilizando BeautifulSoup
site = BeautifulSoup(driver.page_source, 'html.parser')

vagas = site.find_all('div', attrs={'class': 'sc-a3bd7ea-0 HCzvP'})
dados = [] # Cria uma lista dados, que será uma lista de listas, com todos os dados que iremos extrair.
for vaga in vagas:

    # Encontra dados em cada div de vagas e salva em um objeto que posteriormente será parte de uma lista.
    empresa = vaga.find('p', attrs = {'class': "sc-efBctP dpAAMR sc-a3bd7ea-6 cQyvth"}).text
    nome = vaga. find('h2', attrs = {'class': 'sc-llJcti jgKUZ sc-a3bd7ea-5 XNNQK'}).text

    # Aqui em data selecionei apenas os últimos 10 caracteres para salvar apenas dd/mm/aaaa.
    data = vaga.find('p', attrs={'class': 'sc-efBctP dpAAMR sc-1db88588-0 inqtnx'}).text[-10:]

    # Separa o dia, mês e ano.
    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:10]

    # Encontra os três ou quatro atributos: cidade-estado, modelo de trabalho, tipo de trabalho e se possui vaga para pcd.
    atributos= vaga.find_all('div', attrs = {'class': 'sc-23336bc7-2 hCmVmU'})

    # Cria uma lista com os atributos e separa cidade de estado, e cria objetos modelo, tipo, e se tiver quatro elementos
    # na lista, o objeto pcd recebe "Sim".
    lista_atributos= [atributo.text for atributo in atributos]
    if lista_atributos[0] != 'Não informado':
        cidade = lista_atributos[0].split('-')[0]
        estado = lista_atributos[0].split('-')[1]
    else:
        cidade = 'NA'
        estado = 'NA'
    modelo = lista_atributos[1]
    tipo = lista_atributos[2]
    if len(lista_atributos) == 4: pcd = 'Sim'
    else: pcd = 'Não'

    # Guarda o link da vaga.
    link = vaga.find('a', attrs={'class':'sc-a3bd7ea-1 kCVUJf'}).get_attribute_list('href')

    #Insere todos os dados em uma lista de listas.
    dados.append([empresa, nome, modelo, tipo, cidade, estado, dia, mes, ano, pcd, link])

driver.quit()

# Exporta os dados csv, em um DataFrame do Pandas com as 11 variáveis.
df = pd.DataFrame(dados, columns=('Empresa', 'Vaga', 'Modelo', 'Tipo', 'Cidade', 'UF', 'Dia_Publicação', 'Mes_Publicação', 'Ano_Publicação', 'Possui p/ PCD?', 'Link'))
df.to_csv('data.csv', index = False)
