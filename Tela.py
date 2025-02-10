from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from datetime import date
from datetime import datetime

hoje = date.today()

#Importa View
from View import *


#Cores

co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Azul
co4 = "#403d3d" # Cinza
co5 = "#e06636" # Laranja
co6 = "#E9A178" # Laranja Claro
co7 = "#3fbfb9" # Turqueza
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = "#6e8faf"
co11 = "#f2f4f2"
co12 = "#324ebf" # Azul

# Criaçâo da Janela
janela = Tk()
janela.title("")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

#Frames
frameCima = Frame(janela, width=770, height=50, bg=co2, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Icones
app_img = Image.open('library-black.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co2, fg=co1)
app_logo.place(x=5, y=0)

app_texto = Label(frameCima, text="Gerenciamento de Acervo Bibliográfico", 
                  compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), bg=co2, fg=co0)
app_texto.place(x=50, y=7)

app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=('Verdana 1 bold'), bg=co4, fg=co1)
app_linha.place(x=0, y=47)

#Def Novo Usuário
def novo_usuario():
    global img_salvar

    def add():
        p_nome = e_p_n.get()
        s_nome = e_s_n.get()
        email = e_email.get()

        lista = [p_nome, s_nome, email]

        for i in lista:
            #Verificar vazio
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        #Inserindo Dados no BD
        inserir_usuario(p_nome, s_nome, email)

        messagebox.showinfo('Sucesso', 'Usuário Inserido Com Sucesso')

        #Limpando entradas
        e_p_n.delete(0,END)
        e_s_n.delete(0,END)
        e_email.delete(0,END)


    app_ = Label(frameDireita, text="Inserir Novo Usuário", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_p_n = Label(frameDireita, text="Nome:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_n.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_p_n = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_n.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)

    l_s_n = Label(frameDireita, text="Sobrenome:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_s_n.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    e_s_n = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_s_n.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)

    l_email = Label(frameDireita, text="E-mail:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_email.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)
    e_email = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_email.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)

    #Botão Salvar
    img_salvar = Image.open('save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    botao_salvar = Button(frameDireita, command=add,image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' SALVAR',
                     bg=co2, fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    botao_salvar.grid(row=5, column=1, pady=10, sticky=NSEW)


# Ver Usuários
def ver_usuarios():

    app_1 = Label(frameDireita, text="Todos Os Usuários", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_1.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha1 = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha1.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados = get_users()

    #Criando uma visualização em árvore com barras de rolagem duplas
    list_header = ['ID','Nome','Sobrenome','Email']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    #Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw"]
    h=[30,100,170,230]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #Ajusta a largura da coluna de acordo com a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


# Def Novo Livro
def novo_livro():
    global img_salvar1

    def add_livro():
        
        titulo_p = e_titulo.get()
        autor_p = e_autor.get()
        editora_p = e_editora.get()
        ano_p = e_ano.get()

        lista_livro = [titulo_p, autor_p, editora_p, ano_p]

        for i in lista_livro:
            #Verificar vazio
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
            
        #Inserindo Dados no BD
        inserir_livro(titulo_p, autor_p, editora_p, ano_p)

        messagebox.showinfo('Sucesso', 'Livro Inserido Com Sucesso')

        #Limpando entradas
        e_titulo.delete(0,END)
        e_autor.delete(0,END)
        e_editora.delete(0,END)
        e_ano.delete(0,END)

    app_2 = Label(frameDireita, text="Inserir Novo Livro", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_2.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha2 = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha2.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_titulo = Label(frameDireita, text="Título:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_titulo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_titulo = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_titulo.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)

    l_autor = Label(frameDireita, text="Autor:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    e_autor = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)

    l_editora = Label(frameDireita, text="Editora:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)
    e_editora = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)

    l_ano = Label(frameDireita, text="Ano de Publicação:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=10, sticky=NSEW)
    e_ano = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_ano.grid(row=5, column=1, padx=5, pady=10, sticky=NSEW)

    #Botão Salvar
    img_salvar1 = Image.open('save.png')
    img_salvar1 = img_salvar1.resize((18,18))
    img_salvar1 = ImageTk.PhotoImage(img_salvar1)
    botao_salvar1 = Button(frameDireita, command=add_livro,image=img_salvar1, compound=LEFT, width=100, anchor=NW, text=' SALVAR',
                     bg=co2, fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    botao_salvar1.grid(row=6, column=1, pady=10, sticky=NSEW)


# Ver Livros
def ver_livros():
    app_2 = Label(frameDireita, text="Todos Os Livros", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_2.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha2 = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha2.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados2 = exibir_livro()

    #Criando uma visualização em árvore com barras de rolagem duplas
    list_header = ['ID','Título','Autor','Editora', 'Ano']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    #Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw"]
    h=[20,180,150,130,50]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #Ajusta a largura da coluna de acordo com a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados2:
        tree.insert('', 'end', values=item)


# Realizar Empréstimo
def realizar_emprestimo():

    global img_salvar2

    def add_emrestimo():
        
        use_id = e_id_user.get()
        livro_id = e_id_livro.get()

        lista_empretimos = [use_id, livro_id,]

        for i in lista_empretimos:
            #Verificar vazio
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
            
        #Inserindo Dados no BD
        inserir_emprestimo(use_id, livro_id, hoje, None)

        messagebox.showinfo('Sucesso', 'Empréstimo Realizado Com Sucesso')

        #Limpando entradas
        e_id_user.delete(0,END)
        e_id_livro.delete(0,END)


    app_2 = Label(frameDireita, text="Realizar Empréstimo", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_2.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha2 = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha2.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id_user = Label(frameDireita, text="ID do Usuário:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_user.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_user = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_user.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)

    l_id_livro = Label(frameDireita, text="ID do Livro:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_livro = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_livro.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)

    #Botão Salvar
    img_salvar2 = Image.open('save.png')
    img_salvar2 = img_salvar2.resize((18,18))
    img_salvar2 = ImageTk.PhotoImage(img_salvar2)
    botao_salvar2 = Button(frameDireita, command=add_emrestimo,image=img_salvar2, compound=LEFT, width=100, anchor=NW, text=' SALVAR',
                     bg=co2, fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    botao_salvar2.grid(row=6, column=1, pady=10, sticky=NSEW)


# Ver Livros Empretados
def ver_emprestimo():
    app_3 = Label(frameDireita, text="Todos Os Livros Emprestados", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_3.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha3 = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha3.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    dados3 = []

    livros_empretimo = get_livros_empretado()

    for livro in livros_empretimo:
        dado = [f"{livro[3]}", f"{livro[0]}", f"{livro[1]} {livro[2]}", f"{livro[4]}",f"{livro[5]}" ]
        dados3.append(dado)

    #Criando uma visualização em árvore com barras de rolagem duplas
    list_header = ['ID', 'Título', 'Usuário', 'Data Empréstimo', 'Data Devolução']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    #Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw",]
    h=[20,170,150,100,95]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #Ajusta a largura da coluna de acordo com a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados3:
        tree.insert('', 'end', values=item)


# Devolucao de Empréstimo
def devolucao_emprestimo():
   
    global img_salvar3

    def add_devolucao():
        
        empretimo_id = e_id_devolucao.get()
        data_id = e_devolucao.get()

        lista_empretimos = [empretimo_id, data_id,]

        for i in lista_empretimos:
            #Verificar vazio
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
            
        #Inserindo Dados no BD
        atualizar_data_retorno_emprestimo(empretimo_id, data_id)

        messagebox.showinfo('Sucesso', 'Devolução Realizado Com Sucesso')

        #Limpando entradas
        e_id_devolucao.delete(0,END)
        e_devolucao.delete(0,END)


    app_3 = Label(frameDireita, text="Devolução", width=55, compound=LEFT, padx=5, pady=10,
                  font=('Verdana 12'), bg=co2, fg=co0)
    app_3.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha3 = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co4, fg=co1)
    app_linha3.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id_devolucao = Label(frameDireita, text="ID do Empréstimo:", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_devolucao.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_devolucao = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_devolucao.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)

    l_devolucao = Label(frameDireita, text="Data de Devolução (AAAA-MM-DD):", anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_devolucao.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    e_devolucao = Entry(frameDireita, width=25, justify='left', relief='solid')
    e_devolucao.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)

    #Botão Salvar
    img_salvar3 = Image.open('save.png')
    img_salvar3 = img_salvar3.resize((18,18))
    img_salvar3 = ImageTk.PhotoImage(img_salvar3)
    botao_salvar2 = Button(frameDireita, command=add_devolucao,image=img_salvar3, compound=LEFT, width=100, anchor=NW, text=' SALVAR',
                     bg=co2, fg=co0, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    botao_salvar2.grid(row=6, column=1, pady=10, sticky=NSEW) 


# Controle do MENU
def controle(i):
    #novo usuário
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Funcao(novo usuario)
        novo_usuario()

    #ver usuários
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Funcao(ver_usuarios)
        ver_usuarios()

    #novo Livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Funcao(novo livro)
        novo_livro()

    #ver livros
    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Funcao
        ver_livros()

    #Realizar Empréstimo
    if i == 'realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função(emprestimo)
        realizar_emprestimo()
    
    #Ver Livros Empretados
    if i == 'ver_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função(ver_emprestimo)
        ver_emprestimo()

    #devolucao do Empretados
    if i == 'devolucao_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()

        # Chamando Função(devolucao_emprestimo)
        devolucao_emprestimo()


#MENU

#Novo Usuario
img_user = Image.open('user.png')
img_user = img_user.resize((18,18))
img_user = ImageTk.PhotoImage(img_user)
botao_user = Button(frameEsquerda, command=lambda:controle('novo_usuario'), image=img_user, compound=LEFT, anchor=NW, text=' Novo Usuário',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_user.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

#Novo Livro
img_livro = Image.open('add.png')
img_livro = img_livro.resize((18,18))
img_livro = ImageTk.PhotoImage(img_livro)
botao_novo_livro = Button(frameEsquerda, command=lambda:controle('novo_livro'), image=img_livro, compound=LEFT, anchor=NW, text=' Novo Livro',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Livros
ver_livro = Image.open('livro.png')
ver_livro = ver_livro.resize((18,18))
ver_livro = ImageTk.PhotoImage(ver_livro)
botao_ver_livro = Button(frameEsquerda, command=lambda:controle('ver_livros'), image=ver_livro, compound=LEFT, anchor=NW, text=' Acervo',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_ver_livro.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

# Ver Usuarios
ver_user = Image.open('users.png')
ver_user = ver_user.resize((18,18))
ver_user = ImageTk.PhotoImage(ver_user)
botao_ver_user = Button(frameEsquerda, command=lambda:controle('ver_usuarios'), image=ver_user, compound=LEFT, anchor=NW, text=' Todos os Usuários',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_ver_user.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

# Realizar Empréstimo
img_empres = Image.open('send.png')
img_empres = img_empres.resize((18,18))
img_empres = ImageTk.PhotoImage(img_empres)
botao_img_empres = Button(frameEsquerda, command=lambda:controle('realizar_emprestimo'), image=img_empres, compound=LEFT, anchor=NW, text=' Realizar Empréstimo',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_img_empres.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

# Devolução Empréstimo
img_devo = Image.open('return.png')
img_devo = img_devo.resize((18,18))
img_devo = ImageTk.PhotoImage(img_devo)
botao_img_devo = Button(frameEsquerda, command=lambda:controle('devolucao_emprestimo'), image=img_devo, compound=LEFT, anchor=NW, text=' Devolução de Empréstimo',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_img_devo.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

# Livros Emprestados
livros_empres = Image.open('return-purchase.png')
livros_empres = livros_empres.resize((18,18))
livros_empres = ImageTk.PhotoImage(livros_empres)
botao_livros_empres = Button(frameEsquerda, command=lambda:controle('ver_emprestimo'), image=livros_empres, compound=LEFT, anchor=NW, text=' Livros Emprestados',
                     bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
botao_livros_empres.grid(row=7, column=0, sticky=NSEW, padx=5, pady=6)


janela.mainloop()