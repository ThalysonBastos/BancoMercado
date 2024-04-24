import pyodbc #conexao com o banco de dados 

from tkinter import * #importa o modulo para contrucao de interfaces graficas

from tkinter import ttk #importa calsse ttk do modulo tkinter

#Criando a função que verifica se as credenciais estão corretas
def verifica_credenciais():
    #driver - drive
    #Server - Servidor
    #Database - Nome do banco de dados 
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost; Database=Projeto_Compras.db")

    #Ferramenta para executar os comandos SQL 
    cursor = conexao.cursor()

    #UID - Login
    #PWD - Senha
'''    conexao = pyodbc.connect(dadosConexao)
    #testando conexao com print
    print("Conectado com Sucesso! ")
''' 
    #Executando uma query seleciona os usuparios que possui nome e senha inseridos pelo usuário.
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ? ", (nome_usuario_entry.get(), senha_usuario_entry.get()))

    #recebendo o resultado da query acima 
    usuario = cursor.fetchone()


#criando a janela principal para a tela de login 
janela_principal = Tk()
janela_principal.title("Tela de Login")

janela_principal.configure(bg="#F5F5F5") #colocando cor no fundo da janela 

#fg = cor das letras, bg = background cor do fundo
titulo_lbl = Label(janela_principal, text="Tela de Login", font="Arial 20", fg="blue", bg="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20) 
#row = linha, column = coluna, columnspan= colunas que vai ocpuar, pady=espaço

#CAMPO LABEL 
nome_usuario_lbl = Label(janela_principal, text="Nome de Usuário", font="Arial 14 bold", bg="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, sticky="e") # 

#CAMPO LABEL
senha_usuario_lbl = Label(janela_principal, text="Senha", font="Arial 14 bold", bg="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, sticky="e")

#Criando ENTRY para o nome de usuario 
nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row=1, column=1, pady=10)

senha_usuario_entry = Entry(janela_principal, font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10)

entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW") #padx e pady distancias das laterais, stick NSEW ( NORTE SUL LESTE OESTE)
 

sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

#inicia a janela Tkinter
janela_principal.mainloop()









#selecionando tudo da tabela usuários
cursor.execute("Select * From Usuarios")

# passando os dados recebidos para variável valores
valores = cursor.fetchall()

print(valores)

#Inserindo informaç~eos no bd
dados_usuario = ("José", "987")
cursor.execute("INSERT INTO Usuarios (Nome, Senha) Values (?, ?)", dados_usuario )
conexao.commit() # gravando no BD 


#selecionando tudo da tabela usuários
cursor.execute("Select * From Usuarios")

# passando os dados recebidos para variável valores
valores = cursor.fetchall()

print(valores)


#fechando o cursor e a conexao
cursor.close()
conexao.close()





