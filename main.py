from flask import Flask, render_template, request, redirect, url_for, session, abort
import model.Banco.usuario as usuario
from docx import Document
import os 


App = Flask(__name__)
App.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Pagina Principal - Pagina Turmas - get
@App.get("/")
def paginaPrincipal():
        if (verificarLogin(["admin"])):
            seletorAtual = request.args.get("seletor")
            if seletorAtual == None:
                seletor = "*"
                listaAlunos = usuario.ListarAlunos(seletor)
                paginacao = Paginação(listaAlunos)
                return render_template("pageHome.html", alunos = paginacao[0], total_pages = paginacao[1], page = paginacao[2], seletor = seletor, cadastroTrue = False)
            else:
                seletor = seletorAtual
                listaAlunos = usuario.ListarAlunos(seletor)
                paginacao = Paginação(listaAlunos)
                
                return render_template("pageHome.html", alunos = paginacao[0], total_pages= paginacao[1], page = paginacao[2], seletor = seletor)
        else:
            return redirect(url_for('paginaLogin_get'))

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
def cadastrarTurma():
    planilha= request.args.get("planilha")
    cadastroTurmas = usuario.CadastrarTurma(planilha)
    if planilha != None:
        if cadastroTurmas == True:
            return redirect(url_for('paginaPrincipal', cadastro = True))
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
    return redirect(url_for('paginaPrincipal'))

#Gerar Certificado dos Alunos
@App.get("/certificado")
def GerarCertificado():
    id_certificado = request.args.get("id_certificado")
    filename = usuario.GerarCertificado('PI.docx', id_certificado)
    return redirect(url_for('static', filename=f'Certificados/{filename}'))

#Gerar os Certificados de Todos os Alunos
@App.get("/gerarCertificado")
def GerarTodosCertificados():   
    seletor = request.args.get("seletor")
    filename = usuario.GerarTodosCertificados(seletor, 'PI.docx')
    return redirect(url_for('static', filename=f'Certificados/{filename}'))

# CRUD USUARIO-----------------------------------------
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


# Pagina Cadastro -- Get
@App.get("/cadastrar")
def paginaCadastrar_get():
    if (verificarLogin(["admin"])):
        return render_template("pageCadastro.html")
    else:
        return redirect(url_for('paginaLogin_get'))


# Pagina Cadastro -- Post
@App.post("/cadastrar")
def paginaCadastrar_post():
    login = request.form["login"]
    senha = request.form["senha"]
    cadastroUsuario = usuario.CadastrarUsuario(login, senha)
    if(cadastroUsuario == True):
        return render_template("pageCadastro.html", novo_usuario = True)
    else:
        return render_template("pageCadastro.html", novo_usuario = False)


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