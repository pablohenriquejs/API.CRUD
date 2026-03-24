from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def executar_query(query, params=(), fetch=False, commit=False):
    conn = sqlite3.connect('jogos.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    resultado = None
    try:
        cursor.execute(query, params)

        if commit:
            conn.commit()

        if fetch:
            resultado = cursor.fetchall()

    finally:
        conn.close()

    return resultado


# GET - listar todos
@app.route('/jogos', methods=['GET'])
def listar_jogos():
    dados = executar_query("SELECT * FROM jogos", fetch=True)
    return jsonify([dict(item) for item in dados]), 200


# GET - buscar por ID
@app.route('/jogos/<int:id>', methods=['GET'])
def buscar_jogo(id):
    jogo = executar_query(
        "SELECT * FROM jogos WHERE id = ?",
        (id,),
        fetch=True
    )

    if jogo:
        return jsonify(dict(jogo[0])), 200

    return jsonify({"erro": "Jogo não encontrado"}), 404


# POST - inserir
@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()

    executar_query(
        "INSERT INTO jogos (nome, genero, plataforma, preco) VALUES (?, ?, ?, ?)",
        (dados['nome'], dados['genero'], dados['plataforma'], dados['preco']),
        commit=True
    )

    return jsonify({"mensagem": "Jogo adicionado"}), 201


# PUT - atualizar
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    existe = executar_query(
        "SELECT id FROM jogos WHERE id = ?",
        (id,),
        fetch=True
    )

    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "UPDATE jogos SET nome=?, genero=?, plataforma=?, preco=? WHERE id=?",
        (dados['nome'], dados['genero'], dados['plataforma'], dados['preco'], id),
        commit=True
    )

    return '', 204


# DELETE
@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = executar_query(
        "SELECT * FROM jogos WHERE id = ?",
        (id,),
        fetch=True
    )

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "DELETE FROM jogos WHERE id=?",
        (id,),
        commit=True
    )

    return jsonify({"mensagem": "Jogo removido"}), 200


if __name__ == '__main__':
    app.run(debug=True)