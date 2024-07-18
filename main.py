from flask import Flask, render_template, request, redirect, url_for, session
import model.Banco.usuario as usuario
from docx import Document


App = Flask(__name__)
App.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Pagina Principal - Pagina Turmas - get
@App.get("/")
def pagina_principal():
        if (verificarLogin(["admin"])):
            seletorAtual = request.args.get("seletor")
            if seletorAtual == None:
                seletor = "*"
                listaAlunos = usuario.ListarAlunos(seletor)
                paginacao = Paginação(listaAlunos)
                
                return render_template("pageHome.html", alunos = paginacao[0], total_pages = paginacao[1], page = paginacao[2])
            else:
                seletor = seletorAtual
                listaAlunos = usuario.ListarAlunos(seletor)
                paginacao = Paginação(listaAlunos)
                
                return render_template("pageHome.html", alunos = paginacao[0], total_pages= paginacao[1], page = paginacao[2])
        else:
            return redirect(url_for('paginaLogin_get'))


#CRUD ALUNOS-------------------------------------
#Pagina Turmas - Post
@App.post("/")
def cadastrarTurma():
    planilha = request.form["planilha"]
    cadastroTurmas = usuario.CadastrarTurma(planilha)
    if cadastroTurmas == True:
        return render_template("pageHome.html", erro = True)
    else:
         return render_template("pageHome.html", erro = False)


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
    atualizar = usuario.EditarAluno(id_uptade, nome, nomeMae, nomePai, municipioAluno, nacionalidadeAluno, turmaAluno, cpfAluno, rgAluno, cursoAluno)
    return redirect(url_for('paginaEditarAluno_get', id_uptade = id_uptade))


#Delete Aluno
@App.get("/delete")
def DeletarAluno():
    id_Delete =request.args.get("id_delete")
    usuario.Deletar(id_Delete)
    return redirect(url_for('pagina_principal'))


@App.get("/certificado")
def GerarCertificado():
    id_certificado = request.args.get("id_certificado")
    usuario.GerarCertificado('PI.docx', id_certificado)
    return redirect(url_for('pagina_principal'))


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
                return redirect(url_for('pagina_principal'))
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
    page = request.args.get('page', 1, type=int)
    per_page = 16
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(listaAlunos) + per_page - 1) // per_page
                
    items_on_page = listaAlunos[start:end]
    return items_on_page, total_pages, page


App.run(debug=True)