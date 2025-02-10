import sqlite3

# Conectar ao banco de dados
def connet():
    conn = sqlite3.connect('dados.db')
    return conn

# Inserir novo livro
def inserir_livro(titulo, autor, editora, ano_publicacao):
    conn = connet()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao)\
                  VALUES (?,?,?,?)",(titulo, autor, editora, ano_publicacao) )
    conn.commit()
    conn.close()

# Inserir usuários
def inserir_usuario(nome, sobrenome, email):
    conn = connet()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, email)\
                  VALUES(?,?,?)",(nome, sobrenome, email))
    conn.commit()
    conn.close()

# Exibir Usuários
def get_users():
    conn = connet()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Exibir livros 
def exibir_livro():
    conn = connet()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return livros

#Realizar emprestimos
def inserir_emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connet()
    conn.execute("INSERT INTO emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                 VALUES(?,?,?,?)",(id_livro, id_usuario, data_emprestimo, data_devolucao) )
    conn.commit()
    conn.close()

def get_livros_empretado():
    conn = connet()
    result = conn.execute("SELECT emprestimo.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimo.data_emprestimo, emprestimo.data_devolucao\
                          FROM livros\
                          INNER JOIN emprestimo ON livros.id = emprestimo.id_livro\
                          INNER JOIN usuarios ON usuarios.id = emprestimo.id_usuario\
                          WHERE emprestimo.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

def atualizar_data_retorno_emprestimo(id_emprestimo, data_devolucao):
    conn = connet()
    conn.execute("UPDATE emprestimo SET data_devolucao = ? WHERE id =?",(data_devolucao, id_emprestimo ) )
    conn.commit()
    conn.close()

inserir_livro("Ultra Aprendizado", "Scoot H. Young", "Hasper Collins", "2023")
inserir_livro("beserk 5", "Kentaro Miura", "Panini Comics", "1993")
inserir_livro("Trono de vidro", "Sarah J. Maas", "Galera", "2013")
inserir_livro("Overlord Vol. 01", "Hugin Miyama", "Editora JBC", "2021")
inserir_livro("Elden Ring", "Nikiichi Tobita", "Panini", "2022")

inserir_usuario("Dayver", "Richard Silva Lima","dayversilvalima@gmail.com")
inserir_usuario("Claudio", "Roberto lima","claudiolima@gmail.com")
inserir_usuario("Margarete", "Rodrigues","marga_rodri@gmail.com")
inserir_usuario("Pedro", "Gabriel","P8546dro@gmail.com")
inserir_usuario("Matheus", "Alves","alaves_446@gmail.com")