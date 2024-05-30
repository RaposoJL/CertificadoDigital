import model.Banco.BD as conexao
#import BD as conexao


def buscarUsuarioLogin(login, senha):
    conexaoBD = conexao.iniciaConexao()
    query = "SELECT * FROM usuarios WHERE login = %s and senha = %s;"
    parametros = (login, senha) 

    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()
    cursorBD.close()
    conexaoBD.close()
    return listaResultado

def CadastrarUsuario(login, senha):
    conexaoBD = conexao.iniciaConexao()
    query = "SELECT * FROM usuarios WHERE login = %s and senha = %s;"
    parametros = (login, senha) 

    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()

    if(listaResultado == None):
        cadastrar = "INSERT INTO usuarios (login, senha) VALUES (%s, %s);"
        cursorBD.execute(cadastrar, parametros)
        conexaoBD.commit()
    else:
         return False

    cursorBD.close()
    conexaoBD.close()
    