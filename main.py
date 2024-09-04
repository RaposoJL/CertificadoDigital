from flask import Flask, render_template, request, redirect, url_for, session, abort, flash
import model.Banco.usuario as usuario
from docx import Document
import os 
import shutil

def files_path04(path):
    certificadosCriados = []
    for p, _, files in os.walk(os.path.abspath(path)):
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

            return render_template("pageHome.html", alunos = paginacao[0], total_pages= paginacao[1], page = paginacao[2], seletor = seletor, totalAlunos = total, teste = files_path04("static/Certificados"))
        else:
            return redirect(url_for('paginaLogin_get'))
        

<<<<<<< HEAD
#
@App.post("/cadastroTurma")
=======
@App.get("/certificados")
def paginaCertificados():
    return render_template("pageCertificado.html")

#Baixar Planilha Base
@App.get("/baixarPlaninhaBase")
def baixarPlaninha():
    return redirect(url_for('static', filename='midia/PlanilhaBase.xlsx'))

#Pagina Sobre
@App.get("/Sobre")
def paginaSobre():
    return render_template("pageSobre.html")

#CRUD ALUNOS-------------------------------------
#Pagina Turmas - Post
@App.get("/cadastroTurma")
>>>>>>> 5e5b0f0ba90d0072375d70659cf6b3e0771de3e6
def cadastrarTurma():
    planilha = request.files['planilha'] 
    planilha.save(planilha.filename)   
    cadastroTurmas = usuario.CadastrarTurma(planilha)
    os.remove(planilha.filename)

    if planilha != None:
        if cadastroTurmas == True:
<<<<<<< HEAD
            flash("Turma Adicionada com Sucesso!")
            return redirect(url_for('paginaPrincipal'))
=======
            return redirect(url_for('paginaPrincipal', cadastro = True))
>>>>>>> 5e5b0f0ba90d0072375d70659cf6b3e0771de3e6
        else:
            abort(406)
    else:
        abort(404)

#Pagina Editar -- Get
@App.get("/editar")
def paginaEditarAluno_get():
    if (verificarLogin(["admin"])):
        id_uptade = request.args.get("id_uptade")
        uptadeAluno = usuario.ExibirAluno(id_uptade)
        return render_template("pageEditar.html", aluno = uptadeAluno)
    else:
        return redirect(url_for('paginaLogin_get'))


#Pagina Editar -- Post
@App.post("/editar")
def paginaEditarAluno_post():
    id_uptade = request.form["id_uptade"]
    nome = request.form["nomeAluno"]
    nomePai = request.form["nome_paiAluno"]
    nomeMae = request.form["nome_maeAluno"]
    municipioAluno = request.form["municipioAluno"]
    nacionalidadeAluno = request.form["nacionalidadeAluno"]
    turmaAluno = request.form["turmaAluno"]
    cpfAluno = request.form["cpfAluno"]
    rgAluno = request.form["rgAluno"]
    cursoAluno = request.form["cursoAluno"]
    usuario.EditarAluno(id_uptade, nome, nomeMae, nomePai, municipioAluno, nacionalidadeAluno, turmaAluno, cpfAluno, rgAluno, cursoAluno)
    return redirect(url_for('paginaEditarAluno_get', id_uptade = id_uptade))


#Delete Aluno
@App.get("/delete")
def DeletarAluno():
    id_Delete =request.args.get("id_delete")
    usuario.Deletar(id_Delete)
<<<<<<< HEAD
    flash("Aluno Deletado com Sucesso!")
=======
>>>>>>> 5e5b0f0ba90d0072375d70659cf6b3e0771de3e6
    return redirect(url_for('paginaPrincipal'))

#Gerar Certificado dos Alunos
@App.get("/certificado")
def GerarCertificado():
    id_certificado = request.args.get("id_certificado")
    filename = usuario.GerarCertificado('PI.docx', id_certificado)
    flash("Certificado Gerado com Sucesso!")
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
def paginaCadastrar_get():
    if (verificarLogin(["admin"])):
        return render_template("pageCadastroUsuario.html")
    else:
        return redirect(url_for('paginaLogin_get'))


# Pagina Cadastro -- Post
@App.post("/cadastrar")
def paginaCadastrar_post():
    login = request.form["login"]
    senha = request.form["senha"]
    cadastroUsuario = usuario.CadastrarUsuario(login, senha)
    if(cadastroUsuario == True):
        return render_template("pageCadastroUsuario.html", novo_usuario = True)
    else:
        return render_template("pageCadastroUsuario.html", novo_usuario = False)

#END pageCadastroUsuario---------------------------------------------------------------------------------------------------------------


#START pageCertificados------------------------------------------------------------------------------------------------------------------------------------
@App.get("/certificados")
def paginaCertificados():
    certificados = files_path04("static/Certificados")
    certificadosAlunos =  usuario.certificados(certificados)
    return render_template("pageCertificado.html", certificados = certificadosAlunos)


@App.get("/baixarCertificado")
def baixarCertificado():
    idCertificado = request.args.get("idCertificado")
    nomeCertificado = request.args.get("nomeCertificado")
    pastaCertificado = "Certificados/" + idCertificado + "-" + nomeCertificado + ".docx"
    return redirect(url_for('static', filename= pastaCertificado))


@App.get("/deletarCertificado")
def deletarCertificado():
    idCertificado = request.args.get("idCertificado")
    nomeCertificado = request.args.get("nomeCertificado")
    pastaCertificado = "static/Certificados/" + idCertificado + "-" + nomeCertificado + ".docx"
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
        acesso = usuario.LoginUsuario(request.form["login"], request.form["senha"])
        if(acesso != None):
            if (request.form["login"] == acesso[1] and request.form["senha"] == acesso[2]):
                session['logado'] = True
                session['nivel'] = "admin"
                return redirect(url_for('paginaPrincipal'))
            else:   
                return render_template("pageLogin.html", erro=True)
        else:
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