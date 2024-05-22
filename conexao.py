import mysql.connector
conexao = mysql.connector.connect(
            host='localhost',
            database='certificados', 
            user='root', 
            password='')



cursor = conexao.cursor()

# Executar a consulta SQL
cursor.execute("SELECT * FROM responsavel_secretaria")  # Substitua pelo nome da sua tabela

# Obter todos os registros
records = cursor.fetchall()

 # Exibir os registros
print("Total de registros na tabela:", cursor.rowcount)
for row in records:
     print(row)






