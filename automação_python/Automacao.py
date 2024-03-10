# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# biblioteca em Python
# instal pyautogui ->  command prompt -> pip install pyautogui

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 1

# abrir o navegador (chrome)
# aperta a tecla do windows ( command + barra de espaço)
pyautogui.press("win")
# digita o nome do programa (chrome)
pyautogui.write("chrome")
#aperta a tecla enter
pyautogui.press("enter")
# esperar 3 segundos
time.sleep(3)

# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")

# Passo 2 - Fazer login
# Captura posição da tela para clique e-mail
pyautogui.click(x=533, y=412)
# digitar e-mail
pyautogui.write("Automacao@python.com")
# clique senha
pyautogui.press("tab")
# digitar senha
pyautogui.write("senhaautomacao")
# selecionar botao login
pyautogui.press("tab")
# entrar
pyautogui.press("enter")
time.sleep(3)

#Passo 3 - Importar a base de dados
# pip install pandas numpy openpyxl
import pandas as pd

# Importar a base de dados usando pandas
tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    
    # Passo 4 - Cadastrar um produto
    pyautogui.click(x=527, y=296) 
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# repetir isso atpe acabar a base de dados
