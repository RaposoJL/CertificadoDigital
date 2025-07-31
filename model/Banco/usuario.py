import mysql.connector
import model.Banco.conexao as conexao

#INÍCIO CRUD FUNCIONÁRIO==============================================================================
#Função responsável pelo login do usuário
def login_usuario(login, senha):
    conexao_bd = conexao.iniciar_conexao()
    query = "SELECT * FROM funcionario WHERE login = %s and senha = %s;"
    parametros = (login, senha) 

    cursor_bd = conexao_bd.cursor()
    cursor_bd.execute(query, parametros)
    lista_resultado = cursor_bd.fetchone()
    cursor_bd.close()
    conexao_bd.close()

    return lista_resultado


#Função reponsável pelo cadastro de um novo usuário
def cadastrar_usuario(login, senha):
    try:
        conexao_bd = conexao.iniciar_conexao()
        cursor_bd = conexao_bd.cursor()

        cadastrar = "INSERT INTO funcionario (login, senha) VALUES (%s, %s);"
        parametros = (login, senha) 
        cursor_bd.execute(cadastrar, parametros)
        conexao_bd.commit()
        cursor_bd.close()
        conexao_bd.close()
        return True
    except:
        return False


#Função responsável por deleta um usuário já cadastrado
def deletar_usuario(id_usuario):
    conexao_bd = conexao.iniciar_conexao()
    query = 'DELETE FROM funcionario WHERE id = %s;'
    parametro = [id_usuario]
    cursor_bd = conexao_bd.cursor()

    cursor_bd.execute(query, parametro)
    conexao_bd.commit()
    cursor_bd.close()
    conexao_bd.close()


#Função responsável por exibir os usuários cadastrados
def exibir_usuarios():
    lista_usuarios = []
    conexao_bd = conexao.iniciar_conexao()
    query = "SELECT * FROM funcionario"

    cursor_bd = conexao_bd.cursor()
    cursor_bd.execute(query)
    for funcionario in cursor_bd:
        lista_usuarios.append(funcionario)
    cursor_bd.close()
    conexao_bd.close()

    print(lista_usuarios)

    return lista_usuarios

#TÉRMINO CRUD FUNCIONÁRIO==============================================================================