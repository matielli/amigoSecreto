from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def amigo_secreto():
    if request.method == 'POST':
        # Recebe os nomes dos participantes
        nomes = request.form['nomes']
        participantes = [nome.strip() for nome in nomes.split(',') if nome.strip()]
        
        if len(participantes) < 2:
            return render_template('index.html', erro="Adicione pelo menos 2 participantes!")
        
        # Sorteio do amigo secreto
        import random
        sorteio = participantes[:]
        random.shuffle(sorteio)
        
        # Garantir que ninguém se tire a si mesmo
        for i in range(len(participantes)):
            if participantes[i] == sorteio[i]:
                random.shuffle(sorteio)
                i = 0  # Reinicia o loop

        # Criação da lista de pares
        pares = [(participantes[i], sorteio[i]) for i in range(len(participantes))]
        
        return render_template('index.html', pares=pares)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def amigo_secreto():
    if request.method == 'POST':
        # Recebe os nomes dos participantes
        nomes = request.form['nomes']
        participantes = [nome.strip() for nome in nomes.split(',') if nome.strip()]
        
        if len(participantes) < 2:
            return render_template('index.html', erro="Adicione pelo menos 2 participantes!")
        
        # Sorteio do amigo secreto
        import random
        sorteio = participantes[:]
        random.shuffle(sorteio)
        
        # Garantir que ninguém se tire a si mesmo
        for i in range(len(participantes)):
            if participantes[i] == sorteio[i]:
                random.shuffle(sorteio)
                i = 0  # Reinicia o loop

        # Criação da lista de pares
        pares = [(participantes[i], sorteio[i]) for i in range(len(participantes))]
        
        return render_template('index.html', pares=pares)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
