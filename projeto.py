# Passo a passo do projeto
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas


# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/loginMOLO000251 Logitech    Mouse   1   25.95   Hashtag Camisa  2   25.0amisa  1   25.0    11.0        
    

import pyautogui
import time

pyautogui.PAUSE = 0.5
5.0     


pyautogui.press('win')

pyautogui.write('chrome')

pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pyautogui.press('enter')


#2 Logar no site

time.sleep(2)

pyautogui.click(x=1081, y=369)

pyautogui.write('luisao@gmail.com')

pyautogui.press('tab')

pyautogui.write('1234567')

pyautogui.press('tab')

pyautogui.press('enter') 


#3 importar os dados da planilha

import pandas as pas

tabela = pas.read_csv('produtos.csv')
print(tabela)

#4 prencher as lacunas do site

time.sleep(1)

pyautogui.click(x=1107, y=258)

#5 repetir o processo
for linha in tabela.index:
    time.sleep(1)

    pyautogui.click(x=1107, y=258)
    
    #codigo
    pyautogui.write(str(tabela.loc[linha, 'codigo']))

    pyautogui.press('tab')

    #marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))

    pyautogui.press('tab')

    #tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    pyautogui.press('tab')

    #categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    
    pyautogui.press('tab')

    #preco
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))

    pyautogui.press('tab')

    #obs
    
    obs = str(tabela.loc[linha, 'obs'])
    
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')

    #loop
    pyautogui.press('enter')

    pyautogui.scroll(500)