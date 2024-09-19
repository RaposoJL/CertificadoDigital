from flask import Flask, render_template, request, redirect, url_for, session, abort, flash
import model.Banco.usuario as usuario
from docx import Document
import os 
import shutil

def ChecarCertificadosCriados():
    certificadosCriados = []
    caminho = "static/Certificados"

    for p, _, files in os.walk(os.path.abspath(caminho)):
        for file in files:
            idCertificado = (file[:-5].split('-'))
            certificadosCriados.append(idCertificado[0])

    return certificadosCriados
            

App = Flask(__name__)
App.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# START pageHome -------------------------------------------------------------------------------------------------
# Pagina Principal - Pagina Turmas - get
@App.get("/")
def paginaPrincipal():
        if (verificarLogin(["admin"])):
            seletor = request.args.get("seletor")
            listaAlunos = usuario.ListarAlunos(seletor)
            paginacao = Paginação(listaAlunos)
            total = len(listaAlunos)

            return render_template("pageHome.html", alunos = paginacao[0], total_pages= paginacao[1], page = paginacao[2], seletor = seletor, totalAlunos = total)
        else:
            return redirect(url_for('paginaLogin_get'))
        

#paagina Home - Cadastrar Turma
@App.post("/cadastroTurma")
def cadastrarTurma():
    planilha = request.files['planilha']
    planilha.save(planilha.filename)
    
    cadastroTurmas = usuario.CadastrarTurma(planilha)
    os.remove(planilha.filename)

    if cadastroTurmas == True:
        flash("Turma Adicionada com Sucesso!", "concluido")
        return redirect(url_for('paginaPrincipal'))


#Pagina Editar -- Get
@App.get("/editar")
def paginaEditarAluno_get():
    if (verificarLogin(["admin"])):
        id_Aluno = request.args.get("id_Aluno")
        uptadeAluno = usuario.ExibirAluno(id_Aluno)
        return render_template("pageEditar.html", aluno = uptadeAluno)
    else:
        return redirect(url_for('paginaLogin_get'))


#Pagina Editar -- Post
@App.post("/editar")
def paginaEditarAluno_post():
    alunos = usuario.ListarAlunos("*")

    id_Aluno = request.form["id_Aluno"]
    nome = request.form["nomeAluno"]
    nomePai = request.form["nome_paiAluno"]
    nomeMae = request.form["nome_maeAluno"]
    municipioAluno = request.form["municipioAluno"]
    nacionalidadeAluno = request.form["nacionalidadeAluno"]
    turmaAluno = request.form["turmaAluno"]
    cpfAluno = request.form["cpfAluno"]
    rgAluno = request.form["rgAluno"]
    cursoAluno = request.form["cursoAluno"]

    if cpfAluno != cpfAluno:
        for aluno in alunos:
            if cpfAluno == aluno[7]:
                flash("Esse CPF ja pertence a outro aluno!", "erroEditarAluno")
                return redirect(url_for('paginaEditarAluno_get', id_Aluno = id_Aluno))
            elif rgAluno == aluno[8]:
                flash("Esse RG ja pertence a outro aluno!", "erroEditarAluno")
                return redirect(url_for('paginaEditarAluno_get', id_Aluno = id_Aluno))
    else:
        usuario.EditarAluno(id_Aluno, nome, nomeMae, nomePai, municipioAluno, nacionalidadeAluno, turmaAluno, cpfAluno, rgAluno, cursoAluno)
        return redirect(url_for('paginaEditarAluno_get', id_Aluno = id_Aluno))


#Delete Aluno
@App.get("/delete")
def DeletarAluno():
    CertificadosCriados = ChecarCertificadosCriados()
    id_Aluno = request.args.get("id_Aluno")
    infoAluno = usuario.ExibirAluno(id_Aluno)

    for certificado in CertificadosCriados:
        if certificado == id_Aluno:
            flash(f'Este Aluno tem um Certificado Gerado. Apague o Certificado "{id_Aluno} - {infoAluno[1]}" antes de Deletar o Aluno', "erroDeletarAluno")
            return redirect(url_for('paginaPrincipal'))

    usuario.Deletar(id_Aluno)
    flash(f'Aluno {infoAluno[1]} Deletado com Sucesso!', "concluido")
    return redirect(url_for('paginaPrincipal'))

\
#Gerar Certificado dos Alunos
@App.get("/certificado")
def GerarCertificado():
    id_Aluno = request.args.get("id_Aluno")
    usuario.GerarCertificado('PI.docx', id_Aluno)
    infoAluno = usuario.ExibirAluno(id_Aluno)

    flash(f'Certificado de {infoAluno[1]} Gerado com Sucesso!', "concluido")
    return redirect(url_for('paginaPrincipal'))


#Gerar os Certificados de Todos os Alunos
@App.get("/gerarCertificado")
def GerarTodosCertificados():   
    seletor = request.args.get("seletor")
    filename = usuario.GerarTodosCertificados(seletor, 'PI.docx')
    return redirect(url_for('static', filename=f'Certificados/{filename}'))

# END pageHome -------------------------------------------------------------------------------------------------------------

#START pageSobre------------------------------------------------------------------------------------------------------------------------------------
#Baixar Planilha Base
@App.get("/baixarPlaninhaBase")
def baixarPlaninha():
    return redirect(url_for('static', filename='midia/PlanilhaBase.xlsx'))

#Pagina Sobre
@App.get("/Sobre")
def paginaSobre():
    return render_template("pageSobre.html")
#END pageSobrre------------------------------------------------------------------------------------------------------------------------


#START pageCadastroUsuario--------------------------------------------------------------------------------------------------------------------
# Pagina Cadastro -- Get
@App.get("/cadastrar")
def paginaCadastrarUsuario_get():
    if (verificarLogin(["admin"])):
        usuarios = usuario.ExibirUsuarios()
        return render_template("pageCadastroUsuario.html", usuariosCadastrados = usuarios)
    else:
        return redirect(url_for('paginaLogin_get'))
    

#Pagina Cadastro - Deletar Usuario
@App.route("/DeletarUsuario")
def DeletarUsuario():
    id_Usuario = request.args.get("id_Usuario")
    usuario.DeletarUsuario(id_Usuario)
    flash("Usuário Deletado Com Sucesso", "deleteUsuario")
    return redirect(url_for('paginaCadastrarUsuario_post'))







# Pagina Cadastro -- Post
@App.post("/cadastrar")
def paginaCadastrarUsuario_post():
    login = request.form["login"]
    senha = request.form["senha"]

    loginUpper = login.upper()


    cadastroUsuario = usuario.CadastrarUsuario(loginUpper, senha)

    if (cadastroUsuario == True):
        flash("Usuario Cadastrado!","CadastroUsuario") #Flash para mensagem de certo
        return redirect(url_for('paginaCadastrarUsuario_get'))
    else:
        flash('Usuario ou Senha ja Existentes!', "CadastroUsuario") #Flash para mensagem de erro
        return redirect(url_for('paginaCadastrarUsuario_get'))

#END pageCadastroUsuario---------------------------------------------------------------------------------------------------------------


#START pageCertificados------------------------------------------------------------------------------------------------------------------------------------
@App.get("/certificados")
def paginaCertificados():
    certificados = ChecarCertificadosCriados()
    certificadosAlunos =  usuario.certificados(certificados)
    return render_template("pageCertificado.html", certificados = certificadosAlunos)


@App.get("/baixarCertificado")
def baixarCertificado():
    id_Aluno = request.args.get("id_Aluno")
    nomeCertificado = request.args.get("nomeCertificado")
    infoAluno =  usuario.ExibirAluno(id_Aluno)

    CertificadoAluno = "Certificados/" + id_Aluno + "-" + nomeCertificado + ".docx"

    return redirect(url_for('static', filename= CertificadoAluno))


@App.get("/deletarCertificado")
def deletarCertificado():
    id_Aluno = request.args.get("id_Aluno")
    nomeCertificado = request.args.get("nomeCertificado")

    pastaCertificado = "static/Certificados/" + id_Aluno + "-" + nomeCertificado + ".docx"

    os.remove(pastaCertificado)
    flash("Certificado Deletado com Sucesso!")
    return redirect(url_for('paginaCertificados'))

#END pageCertificados------------------------------------------------------------------------------------------------------------------------------------------------

# START pageLogin -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Pagina Login -- Get
@App.get("/login")
def paginaLogin_get():
    return render_template("pageLogin.html")


# Pagina Login -- Post
@App.post("/login")
def paginaLogin_post(): 
        loginUpper = request.form["login"].upper()
        acesso = usuario.LoginUsuario(loginUpper, request.form["senha"])
        if(acesso != None):
            if (loginUpper == acesso[1] and request.form["senha"] == acesso[2]):
                session['logado'] = True
                session['nivel'] = "admin"
                return redirect(url_for('paginaPrincipal'))
            else:
                flash("ERRO LOGIN NÃO EFETUADO", "erroLogin")
                return render_template("pageLogin.html", erro=True)
        else:
            flash("ERRO LOGIN NÃO EFETUADO", "erroLogin")
            return render_template("pageLogin.html", erro=True)

# END pageLogin -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#VERIFICAÇÃO DE PERMISÃO
# Verificar Permisão do Usuario
def verificarLogin(admin):  
    if (('logado' in session) and (session['logado'] == True) and
        ("nivel" in session)):
        for admin in admin:
            if(session["nivel"] == admin):
                return True
        return False
    else:
        return False

# Paginação do Site
def Paginação(listaAlunos):
    per_page = 10
    total_pages = (len(listaAlunos) + per_page) // per_page
    page = request.args.get('page', 1, type=int)

    if page > total_pages:
        page = total_pages - 1

    start = (page - 1) * per_page
    end = start + per_page 
    
    items_on_page = listaAlunos[start:end]
    return items_on_page, total_pages, page


App.run(debug=True)