import json
import psycopg2

# Estabelecer conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="jogos",
    user="postgres",
    password="teste"
)

# Criar um cursor para executar as operações no banco de dados
cursor = conn.cursor()

# Definir a consulta SQL para apagar os dados existentes
delete_query = "DELETE FROM jogos"

# Executar a consulta SQL para apagar os dados existentes
cursor.execute(delete_query)

# Abrir o arquivo JSON contendo os dados
with open('jsondata/soccerstreams.json') as file:
    json_data = json.load(file)

# Percorrer os itens do JSON e inserir no banco de dados
for item in json_data:
    hora = item['hora']
    titulo = item['titulo']
    link = item['link']

    # Definir a consulta SQL para inserção dos dados
    insert_query = "INSERT INTO jogos (hora, titulo, link) VALUES (%s, %s, %s)"
    values = (hora, titulo, link)

    # Executar a consulta SQL com os valores fornecidos
    cursor.execute(insert_query, values)

# Confirmar as alterações no banco de dados
conn.commit()

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
