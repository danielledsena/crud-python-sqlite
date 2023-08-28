import unittest
import sqlite3
from crud import cria_aluno, lista_alunos, atualiza_aluno, deleta_aluno

class TestCrud(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(":memory:")
        self.conexao.execute(''' CREATE TABLE IF NOT EXISTS aluno
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            idade INT NOT NULL); ''')

    def tearDown(self):
        self.conexao.close()

    def test_cria_aluno(self):
        cria_aluno(self.conexao, "Joana", 70)
        cria_aluno(self.conexao, "Talita", 38)
        alunos = self.conexao.execute("SELECT * FROM aluno").fetchall()
        self.assertEqual(len(alunos), 2)
        self.assertEqual(alunos[0][1], "Joana")

    def test_lista_alunos(self):
        cria_aluno(self.conexao, "Joana", 70)
        cria_aluno(self.conexao, "Talita", 38)
        alunos = lista_alunos(self.conexao)
        self.assertEqual(len(alunos), 2)

    def test_atualiza_aluno(self):
        cria_aluno(self.conexao, "Joana", 70)
        cria_aluno(self.conexao, "Talita", 38)
        atualiza_aluno(self.conexao, 1, "Amanda", "27")
        aluno = self.conexao.execute("SELECT * FROM aluno WHERE id = ?", (1,)).fetchone()
        self.assertEqual(aluno[1], "Amanda")

    def test_deleta_aluno(self):
        cria_aluno(self.conexao, "Joana", 70)
        cria_aluno(self.conexao, "Talita", 38)
        deleta_aluno(self.conexao, 1)
        alunos = self.conexao.execute("SELECT * FROM aluno").fetchall()
        self.assertEqual(len(alunos), 1)
        self.assertEqual(alunos[0][1], "Talita")