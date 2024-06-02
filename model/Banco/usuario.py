import model.Banco.BD as conexao
import openpyxl

#Login
def LoginUsuario(login, senha):
    conexaoBD = conexao.iniciaConexao()
    query = "SELECT * FROM usuarios WHERE login = %s and senha = %s;"
    parametros = (login, senha) 

    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()
    cursorBD.close()
    conexaoBD.close()
    return listaResultado


#Cadastrar Novo Ususario

def CadastrarUsuario(login, senha):
    conexaoBD = conexao.iniciaConexao()
    query = "SELECT * FROM usuarios WHERE login = %s and senha = %s;"
    parametros = (login, senha) 

    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()

    if(listaResultado != None):
        cadastrar = "INSERT INTO usuarios (login, senha) VALUES (%s, %s);"
        cursorBD.execute(cadastrar, parametros)
        conexaoBD.commit()
    else:
         return False

    cursorBD.close()
    conexaoBD.close()

#Cadastrar Turma
def CadastrarTurma(planilha):
    book = openpyxl.load_workbook(planilha)
    ws = book.active
    sheet = book['1 - TDS3IN-A']  
    ws.tables

    for table in ws.tables.values():
        print(table)

    num_min = str(10)
    num_max = str(10)
    letra_min = "A"
    letra_max = "I"
    min = letra_min + num_min
    max = letra_max + num_max
    cell_range = sheet[min+':'+ max]
    alunos = []
    for row in cell_range:
         for cell in row:
            alunos.append(cell.value)

    if alunos != None:
        return alunos
    else:
        return "porra meu"