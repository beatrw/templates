#Utilidades gerais - tirar dúvidas e relembrar
#Mexendo com datas, diretórios e arquivos 

import os, glob #Para selecionar fácil coisas de pastas etc
from os.path import getmtime #Para pegar o arquivo mais recente de uma pasta etc
import datetime
import pyexcel #Onde podemos transformar arquivos excel
#import pyexcel as p 
import shutil #Bom para mover arquivos(principalmente entre pastas de rede etc)


# Mexendo com datass
#Pegando o dia anterior por ex
dataHoje =  datetime.datetime.now()#Definindo a data de hoje
dataOntem = dataHoje - datetime.timedelta(days= 1) #Definindo a data de ontem (data de hoje - 1 dia)
dataOntem = dataOntem.strftime("%d/%m/%Y") #Transformando a data em string e mudando a ordem
#Quebrando a data 
dia = dataOntem[:2]
mes = dataOntem[3:5]
ano = dataOntem[6::]

#Para criar pastas - printando erros
try:
    os.mkdir(pasta)
except  FileExistsError as err:
        print(err)

#Listando arquivos e iterando para realizar operações em cada um
listandoArquivos = glob.glob(os.path.join(pasta_destino, "*"))
for arquivo in listandoArquivos:
    try:
        if "aa" in arquivo: #Selecionando arquivo pelo nome 
            os.remove(arquivo) #Removendo
            shutil.move(arquivo, local_destino) #Movendo/renomeando
    except  FileExistsError as err:
        print(err)


#Para pegar arquivo mais recente de uma pasta
arquivo_mais_recente = max(listandoArquivos, key=getmtime)

#Dicas: o shutil e os não funcionam ao tentar transformar um arquivo xls para xlsx, para isso utilizamos o pacote pyexcel
pyexcel.save_book_as (file_name=arquivo, dest_file_name= "destino")   
#p.save_book_as                                               


#Para criar executáveis:
#1-Instala o pacote pyinstaller
#2-Insere o comando: pyinstaller --onefile seuarquivo.py
#O --onefile é para que crie um arquivo só
#Caso exista interação com o usuário, é possível usar o comando: pyinstaller --onefile --windowed seuarquivo.py