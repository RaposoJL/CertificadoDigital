import model.Banco.BD as conexao
import openpyxl
from docx import Document

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
    parametros = (login,senha) 

    cursorBD = conexaoBD.cursor()
    cursorBD.execute(query, parametros)
    listaResultado = cursorBD.fetchone()

    if(listaResultado == None):
        cadastrar = "INSERT INTO usuarios (login, senha) VALUES (%s, %s);"
        cursorBD.execute(cadastrar, parametros)
        conexaoBD.commit()
        cursorBD.close()
        conexaoBD.close()
        return True
    else:
        cursorBD.close()
        conexaoBD.close()
        return False
    


#Cadastrar Turma
def CadastrarTurma(planilha):
    book = openpyxl.load_workbook(planilha)
    ws = book.active
    sheet = book['3º TDS "A"']  
    ws.tables

    num_min = 6
    num_max = 30
    letra_min = "A"
    letra_max = "M"
    alunos = []


    while num_min <= num_max:
        min_col = letra_min + str(num_min)
        max_col = letra_max + str(num_min)
        num_min = num_min + 1
        alunos.clear()
        cell_range = sheet[min_col+':'+ max_col]
        for row in cell_range:
            for cell in row:
                alunos.append(cell.value)

        if (alunos != None):
            conexaoBD = conexao.iniciaConexao()
            query = "INSERT INTO bdalunos (instituicao, nome_completo, cpf, rg, orgao_expedidor, municipio, nacionalidade, data_nascimento, curso, data_conclusão, nome_pai, nome_mae, turma) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            parametros = (alunos[0], alunos[1], alunos[2],alunos[3], alunos[4], alunos[5], alunos[6], alunos[7], str(alunos[8]), str(alunos[9]), alunos[10], alunos[11], alunos[12])

            cursorBD = conexaoBD.cursor()
            cursorBD.execute(query, parametros)
            conexaoBD.commit()
            cursorBD.close()
            conexaoBD.close()
        else:
            return False
    return True


#ListarAlunos
def ListarAlunos(seletor):
    lista = []
    conexaoBD = conexao.iniciaConexao()
    if seletor == "*":
        query = "SELECT * FROM bdalunos"

        cursorBD = conexaoBD.cursor()
        cursorBD.execute(query)
        for aluno in cursorBD:
            lista.append(aluno)
        cursorBD.close()
        conexaoBD.close()
        return lista
    if seletor == "3TDSA":
        query = "SELECT * FROM bdalunos WHERE turma = '3TDSA';"

        cursorBD = conexaoBD.cursor()
        cursorBD.execute(query)
        for aluno in cursorBD:
            lista.append(aluno)
        cursorBD.close()
        conexaoBD.close()
        return lista
    
    if seletor == "3TDSB":
        query = "SELECT * FROM bdalunos WHERE turma = '3TDSB';"

        cursorBD = conexaoBD.cursor()
        cursorBD.execute(query)
        for aluno in cursorBD:
            lista.append(aluno)
        cursorBD.close()
        conexaoBD.close()
        if lista != None:
            return lista
        
    
    if seletor == "3MKTA":
        query = "SELECT * FROM bdalunos WHERE turma = '3MKTA';"

        cursorBD = conexaoBD.cursor()
        cursorBD.execute(query)
        for aluno in cursorBD:
            lista.append(aluno)
        cursorBD.close()
        conexaoBD.close()
        return lista
    
    if seletor == "3MKTB":
        query = "SELECT * FROM bdalunos WHERE turma = '3MKTB';"

        cursorBD = conexaoBD.cursor()
        cursorBD.execute(query)
        for aluno in cursorBD:
            lista.append(aluno)
        cursorBD.close()
        conexaoBD.close()
        return lista

#Exibir Info Alunos -- Editar Alunos
def ExibirAluno(id_uptade):
    conexaoBD = conexao.iniciaConexao()
    query = "SELECT * FROM bdalunos WHERE id = " + str(id_uptade) +";"
    cursorBD = conexaoBD.cursor()

    cursorBD.execute(query)
    infoAluno = cursorBD.fetchone()
    cursorBD.close()
    conexaoBD.close()
    return infoAluno 

#Alterar Info Alunos -- Editar Alunos
def EditarAluno(id_uptade, nome, nomeMae, nomePai, municipioAluno, nacionalidadeAluno, turmaAluno,cpfAluno,rgAluno, cursoAluno):
    conexaoBD = conexao.iniciaConexao()
    query = "UPDATE bdalunos SET nome_completo = %s, nome_mae = %s, nome_pai = %s, municipio = %s, nacionalidade = %s, turma = %s, CPF = %s, rg = %s, curso = %s WHERE id = %s;"
    parametros = (nome, nomeMae, nomePai, municipioAluno, nacionalidadeAluno, turmaAluno, cpfAluno, rgAluno, cursoAluno, id_uptade)
    cursorBD = conexaoBD.cursor()

    cursorBD.execute(query, parametros)
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()

#Deletar Aluno
def Deletar(id_Delete):
    conexaoBD = conexao.iniciaConexao()
    query = 'DELETE FROM bdalunos WHERE id = %s;'
    parametro = [id_Delete]
    cursorBD = conexaoBD.cursor()

    cursorBD.execute(query, parametro)
    conexaoBD.commit()
    cursorBD.close()
    conexaoBD.close()

#Gerar Certificado Individual
def GerarCertificado(documento, id_certificado):
    conexaoBD = conexao.iniciaConexao()
    query = "SELECT * FROM bdalunos WHERE id = " + str(id_certificado) +";"
    cursorBD = conexaoBD.cursor()

    cursorBD.execute(query)
    infoAluno = cursorBD.fetchone()
    cursorBD.close()
    conexaoBD.close()
    
    
    # Carregar o documento existente
    doc = Document(documento)
    substituicoes = {
        '#instituição#': infoAluno[0],
        '#curso#': infoAluno[10],
        '#nome#':  infoAluno[1],
        '#nomeMae#':  infoAluno[2],
        '#nomePai#':  infoAluno[3],
        '#municipio#':  infoAluno[4],
        '#uf#':  infoAluno[9],
        '#nacionalidade#':  infoAluno[5],
        '#diaNas#':  infoAluno[6],
        '#mesNas#': ".",
        '#anoNas#': ".",
        '#cpf#':  infoAluno[7],
        '#rg#':  infoAluno[0],
        '#uf#':  infoAluno[9],
        '#diaCon#':  infoAluno[11],
        '#mesCon#': ".",
        '#anoCon#': ".",
        '#mesNas#': ".",
    }


    # Substituir as palavras em parágrafos
    for para in doc.paragraphs:
        for palavra_antiga, palavra_nova in substituicoes.items():
            if palavra_antiga in para.text: 
                para.text = para.text.replace(palavra_antiga, palavra_nova)


    # Salvar o documento modificado]
    doc.save(infoAluno[1]+ ".docx")