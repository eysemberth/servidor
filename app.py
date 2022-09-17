from urllib import request
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Camila"
    apellido = "Fuentes"
    lista_nombres = [
        "Camila",
        "Marcela"
    ]

    lista_datos = {
        "nombre": nombre,
        "apellido": apellido
    }

    return render_template('index.html', nombre = nombre, lista_nombres = lista_nombres, datos = lista_datos)

@app.route('/mi_pagina')
def mi_pagina():
    datos = [
        "Tanjira",
        "Hamada",
        "demonia@ardiente.com"
    ]

    respuesta = requests.get('https://rickandmortyapi.com/api/character').json()
    results = respuesta['results']
    
    return render_template('mi_pagina.html',  datos = datos, results = results)
