import sqlite3

conexao = sqlite3.connect("aula.db")

conexao.execute(''' CREATE TABLE IF NOT EXISTS aluno
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL); ''')

def cria_aluno(conexao, nome, idade):
    novo_aluno = conexao.execute("INSERT INTO aluno(nome, idade) VALUES (?, ?);", (nome, idade))
    conexao.commit()
    print("Aluno cadastrado com sucesso.")
    return novo_aluno

def lista_alunos(conexao):
    alunos = conexao.execute("SELECT * FROM aluno;").fetchall()
    for aluno in alunos:
        print(aluno)
    return alunos

def atualiza_aluno(conexao, id, novo_nome, nova_idade):
    aluno_atualizado = conexao.execute("UPDATE aluno SET nome = ?, idade = ? WHERE id = ?;", 
                    (novo_nome, nova_idade, id))
    conexao.commit()
    return aluno_atualizado

def deleta_aluno(conexao, id):
    conexao.execute("DELETE FROM aluno WHERE id = ?;", (id,))
    conexao.commit()
    print("Aluno deletado com sucesso.")

lista_alunos(conexao)