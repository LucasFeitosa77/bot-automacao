import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press('win')
pyautogui.write('Brave')
pyautogui.press('enter')

time.sleep(2.1)

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=792, y=465)
pyautogui.write('lucassgabrieel2020@gmail.com')

pyautogui.press('tab')
pyautogui.write('senha extremamente e completamente dificílima')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=748, y=303)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(str(codigo)) #código
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca)) #marca
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo)) #tipo
    pyautogui.press('tab')

    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria)) #categoria
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco_unitario)) #preço
    pyautogui.press('tab')

    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo)) #custo
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    pyautogui.write(str(obs)) #observações
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)