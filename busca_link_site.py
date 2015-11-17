# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:18:02 2015

@author: papacheco
"""
#Baseado:
#https://github.com/realpython/python-scripts

import requests
import re
import os

# get url
url = raw_input("Enter a URL (include `http://`): ")

#Cria variavel de log apartir do nome do site
log = url[7:]

#Arquivo de log
arq = open(log,"w+")

# Conecta a url
website = requests.get(url)

# Leitura html
html = website.text

# re.findall pega todos os links
links = re.findall('"((http|ftp)s?://.*?)"', html)

arq.writelines(links[0])

# Mostra links
for link in links:
    print(link[0])
    
    #Grava em arquivos
    arq.writelines('\n'+link[0])
    