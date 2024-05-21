import pyodbc

from tkinter import *

from tkinter import ttk

#Driver = drive
#Server = servidor
#Database = banco de dados
dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost; Database=Projeto_Compras.db")
#criando a conexao
conexao = pyodbc.connect(dadosConexao)

#cria um objeto cursor para execuar os comandos sql no banco
cursor = conexao.cursor()

#Executa um comando para selecionar todos os produtos
conexao.execute("SELECT * FROM Produtos")

def listar_dados():
    #limpa os valores da treeview
    for i in treeview.get_children():
        treeview.delete(i)

    
    #Executa um comando em SQL para selecionar todos os valores da tabela 
    cursor.execute("Select * from  Produtos")

    #Armazena os valores retornados pelo comando SQL 
    valores = cursor.fetchall()

    #Adiciona os valores na treeview
    for valor in valores:

        #para cada valor de valores, aqui ele popula linha por linha na treeview
        treeview.insert("", "end", values=(valor[0], valor[1], valor[2], valor[3]))

janela = Tk()
janela.title("Cadastro de Produtos")

janela.configure(bg="#FFFFFF")

#deixando a janela em tela cheia 
janela.attributes("-fullscreen", True)

estilo_borda = {"borderwidth": 2, "relief":"groove"}

Label(janela, text="Nome do Produto: ", font="Arial 16", bg="#FFFFFF").grid(row=0, column=2, padx=10, pady=10)
nome_produto = Entry(janela, font="Arial 16", **estilo_borda )
nome_produto.grid(row=0, column=3, padx=10, pady=10)

Label(janela, text="Descrição do Produto: ", font="Arial 16", bg="#FFFFFF").grid(row=0, column=5, padx=10, pady=10)
descricao_produto = Entry(janela, font="Arial 16", **estilo_borda )
descricao_produto.grid(row=0, column=6, padx=10, pady=10)

Label(janela, text="Produtos: ", font="Arial 16", fg="green", bg="#FFFFFF").grid(row=2, column=0, columnspan=10, padx=10, pady=10)


#função para cadastrar o produto
def cadastrar():

    #criando uma nova janela para cadastrar o produto
    janela_cadastrar = Toplevel(janela)
    janela_cadastrar.title("Cadastrar Produtos")

    janela_cadastrar.configure(bg="#FFFFFF") #colocando cor no fundo da janela 

    #define a altura e largura da janela 
    largura_janela = 450
    altura_janela = 250

    #obtendo a largura e altura do computador
    largura_tela = janela_cadastrar.winfo_screenwidth()
    altura_tela = janela_cadastrar.winfo_screenheight()

    #calculando a posição da janela para centraliza-la
    pos_x = (largura_tela // 2 ) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    #definindo a posição da janela
    janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

    for i in range(5):
        janela_cadastrar.grid_rowconfigure(i, weight=1)

    for i in range(2):
        janela_cadastrar.grid_columnconfigure(i, weight=1)


    #adiciona bordas para cada campo de entrada
    estilo_borda = {"borderwidth": 2, "relief":"groove"}

    Label(janela_cadastrar, text="Nome do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")
    nome_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    nome_produto_cadastrar.grid(row=0, column=1, padx=10, pady=10)

    Label(janela_cadastrar, text="Descrição do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, sticky="W")
    descricao_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)

    Label(janela_cadastrar, text="Preço:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, sticky="W")
    preco_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    preco_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)

    #cria uma função para salvar no banco de dados 
    def salvar_dados():
        
        #cria uma tupla com os valores dos campos dos textos
        novo_produto_cadastrar = (nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get())

        cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) VALUES (?, ?, ?)", novo_produto_cadastrar)
        conexao.commit()

        print("Dados Cadastrados com Sucesso !")

        #Fecha a janela
        janela_cadastrar.destroy()

        listar_dados()


    botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
    botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW") #collumspan - quantas colunas vai ocupar

    botao_cancelar = Button(janela_cadastrar, text="Cancelar", font=("Arial", 12), command=janela_cadastrar.destroy)
    botao_cancelar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW") #collumspan - quantas colunas vai ocupar

#Criando um botão abaixo da treeview para cadastrar um novo produto 
botao_gravar = Button(janela, text="Novo", command=cadastrar, font="Arial 18", fg="#2F4F4F", bg="#F8F8FF")
botao_gravar.grid(row=4, column=0, columnspan=4, sticky="NSEW", pady=5, padx=10)

#Define o estilo da treeview
style = ttk.Style(janela)

treeview = ttk.Treeview(janela, style="mystyle.Treeview")

style.theme_use("default")

#Configurando
style.configure("mystyle.Treeview", font=("Arial", 13))

treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("ID", "NomeProduto", "Descricao", "Preco"), show="headings", height=20)
treeview.heading("ID", text="ID")
treeview.heading("NomeProduto", text="Nome do Produto")
treeview.heading("Descricao", text="Descrição do Produto")
treeview.heading("Preco", text="Preço")
#A primeira coluna, identificada como #0
#A opção stretch=NO indica que a coluna não deve esticar 
treeview.column("#0", width=0, stretch=NO)
treeview.column("ID", width=50)
treeview.column("NomeProduto", width=200)
treeview.column("Descricao", width=500)
treeview.column("Preco", width=50)

#columnspan quantas colunas irá ocupar // NSEW preenche as laterais 
treeview.grid(row=3, column=0, columnspan=10, sticky="NSEW")

#chamando a função para listar os dados do banco na treeview 
listar_dados()

def editar_dados(event):

    #obtem o item selecionado na treeview
    item_selecionado = treeview.selection()[0]

    #obtem os valores do item selecionado
    valores_selecionados = treeview.item(item_selecionado)['values']


    #criando uma nova janela para cadastrar o produto
    janela_edicao = Toplevel(janela)
    janela_edicao.title("Cadastrar Produtos")

    janela_edicao.configure(bg="#FFFFFF") #colocando cor no fundo da janela 

    #define a altura e largura da janela 
    largura_janela = 450
    altura_janela = 250

    #obtendo a largura e altura do computador
    largura_tela = janela_edicao.winfo_screenwidth()
    altura_tela = janela_edicao.winfo_screenheight()

    #calculando a posição da janela para centraliza-la
    pos_x = (largura_tela // 2 ) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    #definindo a posição da janela
    janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

    for i in range(5):
        janela_edicao.grid_rowconfigure(i, weight=1)

    for i in range(2):
        janela_edicao.grid_columnconfigure(i, weight=1)


    #adiciona bordas para cada campo de entrada
    estilo_borda = {"borderwidth": 2, "relief":"groove"}

    Label(janela_edicao, text="Nome do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky="W")
    nome_produto_edicao= Entry(janela_edicao, font=("Arial", 12), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[1]))
    nome_produto_edicao.grid(row=0, column=1, padx=10, pady=10)

    Label(janela_edicao, text="Descrição do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, sticky="W")
    descricao_produto_edicao = Entry(janela_edicao, font=("Arial", 12), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[2]))
    descricao_produto_edicao.grid(row=1, column=1, padx=10, pady=10)

    Label(janela_edicao, text="Preço:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, sticky="W")
    preco_produto_edicao = Entry(janela_edicao, font=("Arial", 12), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[3]))
    preco_produto_edicao.grid(row=2, column=1, padx=10, pady=10)

    #cria uma função para salvar no banco de dados 
    def salvar_edicao():
        
        #cria uma tupla com os valores dos campos dos textos
        nome_produto = nome_produto_edicao.get()
        nova_descricao = descricao_produto_edicao.get()
        novo_preco = preco_produto_edicao.get()

        #atualiza os valores dos itens selecionados
        treeview.item(item_selecionado, values=(valores_selecionados[0], nome_produto, nova_descricao, novo_preco))



        cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID = ?",(nome_produto, nova_descricao, novo_preco, valores_selecionados[0]))
        conexao.commit()

        print("Dados Alterados com Sucesso !")

        #Fecha a janela
        janela_edicao.destroy()

        listar_dados()


    botao_salvar_edicao = Button(janela_edicao, text="Alterar", font=("Arial", 16), bg="#3CB371", command=salvar_edicao)
    botao_salvar_edicao.grid(row=4, column=0, padx=20, pady=20) #collumspan - quantas colunas vai ocupar

    botao_deletar_edicao = Button(janela_edicao, text="Deletar", font=("Arial", 16), bg="#F08080", command=janela_edicao.destroy)
    botao_deletar_edicao.grid(row=4, column=1, padx=10, pady=10) #collumspan - quantas colunas vai ocupar


#adiciona o duplo clique na treeviw para editar os dados
treeview.bind("<Double-1>", editar_dados)


menu_barra = Menu(janela)
janela.configure(menu=menu_barra)

#cria o menu chamado arquivo
'''
O parametro "tearoff=0" é utilizado no tkinter para controlar a exibição de uma linha
pontilhada no início de menus cascata,
ao definir "tearoff=0", a linha pontilhada não será exibida e o 
menu cascata ficará fixo na janela, não podendo ser destacado ou movido para outra posição
'''
menu_arquivo = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

#cria uma opção no arquivo de cadastrar
menu_arquivo.add_command(label="Cadastrar", command=cadastrar)
#criando o sair
menu_arquivo.add_command(label="Sair", command=janela.destroy)

#Criando um botão abaixo da treeview para cadastrar um novo produto 
botao_delete = Button(janela, text="Deletar", command=cadastrar, font="Arial 18", fg="#2F4F4F", bg="#F8F8FF")
botao_delete.grid(row=4, column=4, columnspan=4, sticky="NSEW", padx=5, pady=5)


#inicia a janela Tkinte
janela.mainloop()
#fechando o cursor e a conexao
cursor.close()
conexao.close()
