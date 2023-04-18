from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Define o endpoint '/nome'
@app.route('/nomes')

def get_nome():
    # Carrega o arquivo JSON
    with open('Data/lista_de_nomes.json') as f:
        data = json.load(f)

    # Extrai a lista de nomes completos
    lista_nomes = data['nomes']
    lista_sobrenomes = data['sobrenomes']

    # Monta o nome completo
    #nome_completo = random.choice(lista_nomes) + ' ' + random.choice(lista_sobrenomes)
    
    # Retorna o nome selecionado em formato JSON
    return jsonify({'nome': random.choice(lista_nomes) + ' ' + random.choice(lista_sobrenomes) })

app.run(port=50000, host='localhost')