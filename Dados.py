import sqlite3

# Conectar ao banco de dados e Criar as Tabelas (Usuários, Livros, Empréstimo)
con = sqlite3.connect('dados.db')

con.execute('CREATE TABLE usuarios(\
            id INTEGER PRIMARY KEY,\
            nome TEXT,\
            sobrenome TEXT,\
            email TEXT)')

con.execute('CREATE TABLE livros(\
            id INTEGER PRIMARY KEY,\
            titulo text,\
            autor TEXT,\
            editora TEXT,\
            ano_publicacao INTEGER)')

con.execute('CREATE TABLE emprestimo(\
            id INTEGER PRIMARY KEY,\
            id_usuario INTEGER,\
            id_livro INTEGER,\
            data_emprestimo TEXT,\
            data_devolucao TEXT,\
            FOREIGN KEY(id_livro) REFERENCES livros(id),\
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')

