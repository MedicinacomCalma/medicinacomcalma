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

html_home = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medicina com Calma</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #fdfdfd;
            color: #333;
        }
        header {
            background-color: #ffffff;
            padding: 30px 0;
            text-align: center;
            border-bottom: 2px solid #f1f1f1;
        }
        header h1 {
            color: #254E70;
            font-size: 2.2rem;
        }
        header p {
            color: #F57C73;
            font-size: 1.1rem;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            padding: 40px;
            max-width: 1100px;
            margin: auto;
        }
        .card {
            background-color: #ffffff;
            border-radius: 20px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            padding: 20px;
            text-align: center;
            transition: transform 0.3s;
        }
        .card:hover {
            transform: scale(1.02);
        }
        .card img {
            max-width: 100%;
            border-radius: 12px;
            margin-bottom: 15px;
        }
        .card h3 {
            font-size: 1.1rem;
            color: #254E70;
            margin-bottom: 10px;
        }
        .card p {
            font-size: 0.95rem;
            color: #555;
            margin-bottom: 10px;
        }
        .preco {
            font-size: 1.1rem;
            font-weight: bold;
            color: #F57C73;
            margin-bottom: 10px;
        }
        .botao {
            background-color: #254E70;
            color: #fff;
            padding: 10px 20px;
            border-radius: 10px;
            text-decoration: none;
            display: inline-block;
        }
        footer {
            text-align: center;
            padding: 30px;
            font-size: 0.9rem;
            color: #aaa;
        }
    </style>
</head>
<body>
    <header>
        <h1>Medicina com Calma</h1>
        <p>Conteúdos médicos acessíveis, bonitos e didáticos</p>
    </header>

    <div class="container">
        {% for produto in produtos %}
        <div class="card">
            <img src="{{ produto['imagem'] }}" alt="{{ produto['titulo'] }}">
            <h3>{{ produto['titulo'] }}</h3>
            <p>{{ produto['descricao'] }}</p>
            <div class="preco">{{ produto['preco'] }}</div>
            <a href="https://wa.me/5583999999999" class="botao">Comprar no WhatsApp</a>
        </div>
        {% endfor %}
    </div>

    <footer>
        &copy; 2025 Medicina com Calma. Todos os direitos reservados.
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_home, produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
