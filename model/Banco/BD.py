import mysql.connector

def iniciaConexao():
    conexaoBanco = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="certificados"
    )
    
    return conexaoBanco

