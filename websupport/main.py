import subprocess
from flask import Flask, render_template, request, jsonify
import psycopg2
import os

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
    cursor.execute("SELECT * FROM jogos ORDER BY hora LIMIT %s OFFSET %s", (per_page, offset))
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
    cursor.execute("SELECT * FROM jogos ORDER BY hora")
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

@app.route("/gerar-json", methods=["GET"])
def gerar_json():
     # Definir o diretório do Scrapy
    
    main_directory = os.getcwd()
    scrapy_directory = "sportstreaming"

    # Alterar o diretório atual para o diretório do Scrapy
    os.chdir(scrapy_directory)
   

    # Executar o comando do Scrapy para gerar o arquivo JSON
    subprocess.run(["scrapy crawl soccerstreams -O /home/wock/Documents/GitHub/Finder-Project/websupport/sportstreaming/database/jsondata/soccerstreams.json"], shell=True)

    os.chdir(main_directory)
    return "Arquivo JSON gerado com sucesso!"

@app.route("/inserir-json", methods=["GET"])
def inserir_json():
     # Definir o diretório da Base de DAdos
    main_directory = os.getcwd()
    db_directory = "sportstreaming/database"
    

    # Alterar o diretório atual para o diretório do Scrapy
    os.chdir(db_directory)

    # Executar o comando do Scrapy para gerar o arquivo JSON
    subprocess.run(["python3 db.py"], shell=True)

    os.chdir(main_directory)
    return "Arquivo JSON inserido com sucesso na base de dados!"

@app.route("/apagar-dados", methods=["GET"])
def apagar_dados():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jogos")
    conn.commit()
    cursor.close()
    return "Dados apagados com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
