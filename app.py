from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '123'

usuarios = []
atletas = []

# HOME
@app.route('/')
def index():
    return render_template('index.html')

# CADASTRO
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']
        usuarios.append({'user': user, 'senha': senha})
        return redirect('/login')
    return render_template('cadastro.html')

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None

    if request.method == 'POST':
        user = request.form.get('user')
        senha = request.form.get('senha')

        for u in usuarios:
            if u['user'] == user and u['senha'] == senha:
                session['user'] = user
                return redirect('/atletas')

        erro = "Usuário ou senha inválidos"

    return render_template('login.html', erro=erro)

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# LISTAR ATLETAS
@app.route('/atletas')
def atletas_lista():
    if 'user' not in session:
        return redirect('/login')

    busca = request.args.get('busca')

    if busca:
        lista = [a for a in atletas if busca.lower() in a['nome'].lower()]
    else:
        lista = atletas

    return render_template('atletas.html', atletas=lista)

# ADICIONAR
@app.route('/add', methods=['GET', 'POST'])
def add_atleta():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        esporte = request.form['esporte']

        atletas.append({
            'id': len(atletas),
            'nome': nome,
            'idade': idade,
            'esporte': esporte
        })

        return redirect('/atletas')

    return render_template('form_atleta.html')

# EDITAR
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar_atleta(id):
    if 'user' not in session:
        return redirect('/login')

    atleta = atletas[id]

    if request.method == 'POST':
        atleta['nome'] = request.form['nome']
        atleta['idade'] = request.form['idade']
        atleta['esporte'] = request.form['esporte']
        return redirect('/atletas')

    return render_template('form_atleta.html', atleta=atleta)

# REMOVER
@app.route('/delete/<int:id>')
def deletar_atleta(id):
    if 'user' not in session:
        return redirect('/login')

    atletas.pop(id)
    return redirect('/atletas')

if __name__ == '__main__':
    app.run(debug=True)