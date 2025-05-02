import sqlite3
from datetime import datetime

class AcessoDB:
    def __init__(self, db_path="acessos.db"):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS acessos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    data TEXT
                )
            """)
            con.commit()

    def registrar_acesso(self, nome):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO acessos (nome, data) VALUES (?, ?)", (nome, datetime.now().isoformat()))
            con.commit()
