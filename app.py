from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'medicinacomcalma2025'

USUARIO = 'giovana'
SENHA = 'calma123'

produtos = [
    {
        'titulo': 'Descomplicando a Histologia com Giovana',
        'descricao': 'Resumo ilustrado com passo a passo do uso do microscópio, linguagem leve e atividade final.',
        'preco': 'R$ 25,00',
        'imagem': 'https://files.oaiusercontent.com/file_00000000718861f99b8ce9b01101784e.png'
    },
]

html_home = """<!doctype html><html lang='pt-br'><head><meta charset='utf-8'><title>Medicina com Calma</title>
<style>body{font-family:sans-serif;padding:0;margin:0;background:#fdfdfd;}header{background:white;text-align:center;padding:20px;box-shadow:0 2px 5px rgba(0,0,0,0.1);}h1{color:#254E70;}h2{color:#F57C73;}footer{text-align:center;color:#999;padding:20px;font-size:0.9em;}.produtos{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;padding:20px;max-width:1000px;margin:auto;}.produto{background:white;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,0.05);padding:20px;text-align:center;}.produto img{max-width:100%;border-radius:10px;}.preco{color:#F57C73;font-weight:bold;margin:10px 0;}.botao{background:#254E70;color:white;padding:10px 15px;border-radius:10px;text-decoration:none;display:inline-block;margin-top:10px;}</style></head>
<body><header><h1>Medicina com Calma</h1><h2>Conteúdos médicos acessíveis e bonitos</h2></header>
<div class='produtos'>{% for produto in produtos %}
  <div class='produto'><img src='{{ produto["imagem"] }}' alt='{{ produto["titulo"] }}'>
    <h3>{{ produto['titulo'] }}</h3><p>{{ produto['descricao'] }}</p>
    <div class='preco'>{{ produto['preco'] }}</div>
    <a href='https://wa.me/5583999999999' class='botao'>Comprar no WhatsApp</a>
  </div>{% endfor %}</div><footer>&copy; 2025 Medicina com Calma</footer></body></html>"""

html_login = """<!doctype html><html><head><meta charset='utf-8'><title>Login</title>
<style>body{font-family:sans-serif;background:#f0f0f0;display:flex;justify-content:center;align-items:center;height:100vh;}form{background:white;padding:30px;border-radius:10px;box-shadow:0 0 10px rgba(0,0,0,0.1);}input{margin-bottom:10px;padding:10px;width:100%;border:1px solid #ccc;border-radius:5px;}button{padding:10px 20px;background:#254E70;color:white;border:none;border-radius:5px;cursor:pointer;}</style></head>
<body><form method='post'><h2>Login</h2><input type='text' name='usuario' placeholder='Usuário'><input type='password' name='senha' placeholder='Senha'><button type='submit'>Entrar</button></form></body></html>"""

html_admin = """<!doctype html><html><head><meta charset='utf-8'><title>Administração</title>
<style>body{font-family:sans-serif;padding:40px;background:#fdfdfd;}form{max-width:500px;margin:auto;}input{display:block;margin:10px 0;padding:10px;width:100%;}button{padding:10px;background:#254E70;color:white;border:none;border-radius:5px;}</style></head>
<body><h2>Adicionar novo produto</h2><form method='post'><input name='titulo' placeholder='Título'><input name='descricao' placeholder='Descrição'><input name='preco' placeholder='Preço'><input name='imagem' placeholder='Link da imagem'><button type='submit'>Salvar</button></form><p><a href='/'>Voltar ao site</a></p></body></html>"""

@app.route("/")
def home():
    return render_template_string(html_home, produtos=produtos)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form['usuario'] == USUARIO and request.form['senha'] == SENHA:
            session['logado'] = True
            return redirect("/admin")
    return render_template_string(html_login)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get('logado'):
        return redirect("/login")
    if request.method == "POST":
        novo = {
            'titulo': request.form['titulo'],
            'descricao': request.form['descricao'],
            'preco': request.form['preco'],
            'imagem': request.form['imagem']
        }
        produtos.append(novo)
        return redirect("/")
    return render_template_string(html_admin)

if __name__ == '__main__':
    app.run(debug=True)