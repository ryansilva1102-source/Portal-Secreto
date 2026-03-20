from flask import Flask, render_template, jsonify
import random
from datetime import datetime

app = Flask(__name__)

futuros_roles = [
    {"nome": "Piquenique e caminhada no Ibirapuera 🌳☀️", "imagem": "role-ibira.jpg"},
    {"nome": "Explorar um restaurante novo em São Paulo 🍝🍷", "imagem": "role-restaurante.jpg"},
    {"nome": "Ida ao cinema com namoradeira em São Paulo 🍿🎥", "imagem": "role-cinema.jpg"},
    {"nome": "Passeio de domingo na Avenida Paulista com direito a sorvete 🍦🏙️", "imagem": "role-paulista.jpg"},
    {"nome": "Noite de boliche ou fliperama para ver quem ganha 🎳👾", "imagem": "role-jogos.jpg"},
    {"nome": "Passar a tarde a passear na Liberdade e provar várias comidas diferentes 🏮🍡", "imagem": "role-liberdade.jpg"} # <-- A sua escolha com texto natural!
]
@app.route('/')
def home():
    # Ajuste a data em que se conheceram
    data_conhecemos = datetime(2025, 11, 2, 0, 0, 0)
    
    # Ajuste a data do primeiro beijo
    data_beijo = datetime(2026, 2, 14, 0, 0, 0)

    agora = datetime.now()
    
    diferenca_conhecemos = agora - data_conhecemos
    diferenca_beijo = agora - data_beijo

    # Usando o atributo .days para pegar apenas o número de dias inteiros
    dias_conhecemos = diferenca_conhecemos.days
    dias_beijo = diferenca_beijo.days
    
    # Agora você passa 'dias_conhecemos' e 'dias_beijo' para o seu template HTML
    # Extraímos só os nomes para a roleta girar no visual
    nomes_roles = [role['nome'] for role in futuros_roles]

    return render_template('index.html', 
                            dias_conhecemos=dias_conhecemos, 
                            dias_beijo=dias_beijo,
                            roles=nomes_roles)

@app.route('/sortear')
def sortear():
    # Sorteia um pacote completo (nome + imagem)
    role_escolhido = random.choice(futuros_roles)
    return jsonify({
        'role_sorteado': role_escolhido['nome'],
        'imagem_sorteada': role_escolhido['imagem']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
