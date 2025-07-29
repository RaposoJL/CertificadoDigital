import mysql.connector

#Função responsável por iniciar conexão com o banco de dados
def iniciar_conexao():
    conexao_bd = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="certificado_digital_novo"
    )
    
    return conexao_bd