import pyodbc


#driver - drive
#Server - Servidor
#Database - Nome do banco de dados 

dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost; Database=Projeto_Compras.db")

#UID - Login
#PWD - Senha

conexao = pyodbc.connect(dadosConexao)

#testando conexao com print
print("Conectado com Sucesso! ")

#Ferramenta para executar os comandos SQL 
cursor = conexao.cursor()

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





