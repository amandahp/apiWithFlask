# Definindo padrão de codificação
# coding: utf-8

#Importação do microFramework Flask
from flask import Flask

#Criação da aplicação web, passando como paramêtro o nome do projeto em questão
app = Flask('projeto1')

#Decorator que define a rota dessa função
@app.route("/")
#Criação de uma função simples em Python
def hello_world():
    #resultado que será apresentado na página
    return "Hello World! This is my first WebApp", 200

#comando para rodar aplicação 
app.run()

