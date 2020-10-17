# Definindo padrão de codificação
# coding: utf-8

#Importação do microFramework Flask
from flask import Flask, render_template

#Criação da aplicação web, passando como paramêtro o nome do projeto em questão
app = Flask('projeto1')

#Decorator que define a rota dessa função
@app.route("/condicional/")
#Criação de uma função simples em Python
def condicional():
    #meu_nome = "amanda"
    #resultado que será apresentado na página
    return render_template("modelo_condicional.html"), 200 #nome=meu_nome), 200

#comando para rodar aplicação 
app.run()

