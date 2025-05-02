import sqlite3
from datetime import datetime

def criar_tabela():
    con = sqlite3.connect("acessos.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS acessos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data TEXT
        )
    """)
    con.commit()
    con.close()

def registrar_acesso(nome):
    con = sqlite3.connect("acessos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO acessos (nome, data) VALUES (?, ?)", (nome, datetime.now().isoformat()))
    con.commit()
    con.close()
