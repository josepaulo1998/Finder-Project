from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuração do banco de dados
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="jogos",
    user="postgres",
    password="teste"
)

@app.route("/")
def index():
    # Obter o número da página atual a partir do parâmetro da URL
    page = int(request.args.get("page", 1))

    # Definir o número de jogos por página
    per_page = 10

    # Calcular o deslocamento para a consulta SQL
    offset = (page - 1) * per_page

    # Exemplo de rota para exibir dados da tabela com paginação
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jogos LIMIT %s OFFSET %s", (per_page, offset))
    data = cursor.fetchall()

    # Obter o número total de jogos
    cursor.execute("SELECT COUNT(*) FROM jogos")
    total_count = cursor.fetchone()[0]

    # Calcular o número total de páginas
    total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)

    cursor.close()
    return render_template("index.html", data=data, current_page=page, total_pages=total_pages)

@app.route("/atualizar", methods=["GET"])
def atualizar():
    # Exemplo de rota para atualizar os dados da tabela
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jogos")
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route("/add", methods=["GET", "POST"])
def add():
    # Exemplo de rota para adicionar dados à tabela
    if request.method == "POST":
        titulo = request.form.get("titulo")
        nome = request.form.get("nome")
        link = request.form.get("link")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO jogos (titulo, nome, link) VALUES (%s, %s, %s)", (titulo, nome, link))
        conn.commit()
        cursor.close()

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)