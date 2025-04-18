import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tabuada_ai"
    )

def registrar_resposta(pergunta, resposta, correta):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO respostas (pergunta, resposta, correta) VALUES (%s, %s, %s)"
    cursor.execute(sql, (pergunta, resposta, correta))
    db.commit()
    db.close()

def pegar_respostas_erradas():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT pergunta FROM respostas WHERE correta = 0")
    resultados = cursor.fetchall()
    db.close()
    return [row[0] for row in resultados]
