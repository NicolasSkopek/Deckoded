import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_name="deckoded.db"):
        self.db_name = db_name
        self._criar_tabela()


    def _conectar(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        return conn, cursor

    def _criar_tabela(self):
        conn, cursor = self._conectar()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jogador TEXT NOT NULL,
                pontuacao INTEGER NOT NULL,
                data TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def salvar_resultado(self, jogador, pontuacao):
        conn, cursor = self._conectar()
        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO resultados (jogador, pontuacao, data) VALUES (?, ?, ?)",
            (jogador, pontuacao, data_atual)
        )
        conn.commit()
        conn.close()

    def resetar_banco(self):
        conn, cursor = self._conectar()
        cursor.execute("DROP TABLE IF EXISTS resultados")
        conn.commit()
        conn.close()
        self._criar_tabela()

    def listar_resultados(self, limite=10):
        conn, cursor = self._conectar()
        cursor.execute(
            "SELECT jogador, pontuacao, data FROM resultados ORDER BY pontuacao DESC LIMIT ?",
            (limite,)
        )
        resultados = cursor.fetchall()
        conn.close()
        return resultados