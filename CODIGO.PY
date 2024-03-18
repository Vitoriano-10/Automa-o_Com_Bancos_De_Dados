            # PASSO A PASSO 
#BIBLIOTECA PARA DEIXAR AUTOMATICO - PYAUTOGUI
# PYAUTOGUI.PRESS - APERTAR UMA TECLA
# PYAUTOGUI.WRITE - ESCREVER UM TEXTO OU PALAVRA
# PYAUTOGUI.CLICK - CLICAR COM O MOUSE EM ALGUM LUGAR DA TELA

#PASSO 1 - ABRIR O SITE PARA CADASTRAR OS ITENS
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
#PASSO 1.1 - IMPORTAR A BLIBLIOTECA PARA AUTOMATIZAR
import pyautogui
import time

pyautogui.PAUSE =1

#PASSO 1.2 - ABRIR O CHROME

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
#PASSO 1.3 - ABRIR O SITE
link= 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('Enter')
#DEIXAR O LINK COMO VARIAVEL PARA CASO ELE MUDE NAO TENHAMOS PROBMLEMAS

#PASSO 2 - FAZER O LOGIN NO SITE

#PASSO 2.1 - DAR UMA PAUSA MAIOR 
time.sleep(2) 
#PASSO 2.2 - FAZER CLICAR NO CAMPO PRIMEIRO CAMPO E PREENCHER
pyautogui.click(x=476, y=409)
pyautogui.write('sasagueyo@gmail.com')
#PASSO 2.3 - PASSAR PARA O CAMPO DE BAIXO E PREENCHER
pyautogui.press('tab')
pyautogui.write('minhasenha@')
#PASSO 2.4 - CLICAR PARA LOGAR
pyautogui.press('tab')
pyautogui.press('Enter')
time.sleep(2)

#PASSO 3 - IMPORTAR A BASE DE DADOS

# FERRAMENTA PARA IMPORTAR - pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("tabela.csv")
print(tabela)

#PASSO 4 - CADASTRAR O PRIMEIRO PRODUTO
#LOOP PARA REFAZER TODOS OS PROCESSOS NOVAMENTE - ESTRUTURA DE REPETIÇÃO
for linha in tabela.index:
    
    #PASSO 4.1 - CLICAR NA PRIMEIRA OPÇÃO DO PRODUTO
    pyautogui.click(x=499, y=293)
    #PASSO 4.2 EM DIANTE - CADASTRAR OS CAMPOS COM AS INFORMÇÕES
    
    # CODIGO DO PRODUTO
    #LOC É PARA LOCALIXAR DENTRO DA TABELA
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab') 
    
    # MARCA
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')
    
    # TIPO
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')
    
    # CATEGORIA
    categoria = tabela.loc[linha, "categoria"]
    #PRECISA TRANSFORMAR O VALOR EM STRING: srt()
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    
    # PREÇO UNITARIO
    preco = tabela.loc[linha, "preco_unitario"]
    #PRECISA TRANSFORMAR O VALOR EM STRING: srt()
    pyautogui.write(str(preco))
    pyautogui.press('tab')
    
    # CUSTO  
    custo = tabela.loc[linha, "custo"]
    #PRECISA TRANSFORMAR O VALOR EM STRING: srt()
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    
    # OBS
    #PRECISA COLOCAR UMA CONDIÇÃO POIS NEM TODOS OS ITENS POSSUEM UMA OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    
    # ENVIAR 
    pyautogui.press('enter')
    #VOLTAR PRO INICIO
    
    pyautogui.scroll(2000)

#PASSO 5 - REPETIR O PROCESSO ATE ACABAR OS PRODUTOS

