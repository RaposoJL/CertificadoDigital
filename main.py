from flask import Flask, app, render_template, request, redirect, url_for, session, abort, flash
import model.Banco.certificado as certificado
import model.Banco.usuario as usuario
import model.Banco.aluno as aluno
from docx import Document
import os 
import shutil

App = Flask(__name__)
App.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#adicionar Certificado
@App.post("/adicionar_doc_certificado")
def adicionarDocCertificado():
    documentoCertificado = request.files['documentoCertificado']
    
    documentoCertificado.save(documentoCertificado.filename)
    return documentoCertificado


@App.get("/")
def paginaIntroducao():
        if (verificarLogin(["admin"])):
            seletor = request.args.get("seletor")
            lista_alunos = aluno.listar_alunos(seletor)
            lista_certificados = checarCertificadosCriados()
            paginacao_pp = paginacao(lista_alunos)
            total = len(lista_alunos)

            return render_template("pageIntroducao.html", alunos = paginacao_pp[0], 
                                   total_pages= paginacao_pp[1], 
                                   page = paginacao_pp[2], 
                                   seletor = seletor, 
                                   total_alunos = total,
                                   certificados = lista_certificados,
                                   pesquisa = False)
        else:
            return redirect(url_for('paginaLogin_get'))   


# Pagina Principal - Pagina Turmas - get
@App.get("/inicio")
def paginaInicial():
        if (verificarLogin(["admin"])):
            seletor = request.args.get("seletor")
            lista_alunos = aluno.listar_alunos(seletor)
            lista_certificados = checarCertificadosCriados()
            paginacao_pp = paginacao(lista_alunos)
            total = len(lista_alunos)

            return render_template("pageHome.html", alunos = paginacao_pp[0], 
                                   total_pages= paginacao_pp[1], 
                                   page = paginacao_pp[2], 
                                   seletor = seletor, 
                                   total_alunos = total,
                                   certificados = lista_certificados,
                                   pesquisa = False)
        else:
            return redirect(url_for('paginaLogin_get'))        


@App.get("/turmas")
def paginaTurmas():
        if (verificarLogin(["admin"])):
            seletor = request.args.get("seletor")
            lista_alunos = aluno.listar_alunos(seletor)
            lista_certificados = checarCertificadosCriados()
            paginacao_pp = paginacao(lista_alunos)
            total = len(lista_alunos)

            return render_template("pageTurmas.html", alunos = paginacao_pp[0], 
                                   total_pages= paginacao_pp[1], 
                                   page = paginacao_pp[2], 
                                   seletor = seletor, 
                                   total_alunos = total,
                                   certificados = lista_certificados,
                                   pesquisa = False)
        else:
            return redirect(url_for('paginaLogin_get'))     


#Responsável por direcionar e realizar a busca pelo aluno 
@App.post("/pesquisar_aluno")
def pesquisarAluno():
    nome_aluno = request.form["nome_completo"]
    resultado = certificado.pesquisar_aluno(nome_aluno)
    paginacao_pp = paginacao(resultado)
    seletor = None
    total = len(resultado)
    return render_template("pageTurmas.html", alunos = paginacao_pp[0],
                           total_pages = paginacao_pp[1],
                           page = paginacao_pp[2],
                           total_alunos = total,
                           seletor = seletor,
                           pesquisa = True)
    

#
@App.get("/apagar_todos_alunos")
def deletarTodosAlunos():
    certificados = checarCertificadosCriados()
    alunos = aluno.listar_alunos("*")
    if alunos == []:
        flash("Nenhum Aluno Existente", "erro")
        return redirect(url_for('paginaTurmas'))
    else:
        if certificados == []:
            aluno.deletar_todos_alunos(alunos)
            flash("Todos os Alunos Deletados", "concluido")
            return redirect(url_for('paginaTurmas'))
        else:
            flash("Delete Todos os Certificados Antes dessa Ação", "erro")
            return redirect(url_for('paginaTurmas'))


#=====================================================================================================================
#Responsável por pegar a planilha com as informações dos alunos de cada turma 
@App.post("/cadastro_turma")
def cadastrarTurma():
    planilha = request.files["planilha"]
    sheet = request.form["sheet"]
    
    planilha.save(planilha.filename)
    cadastro_turmas = aluno.cadastrar_turma_alunos(planilha.filename)

    if cadastro_turmas != False:
        os.remove(planilha.filename)
        flash(f'Planilha {planilha.filename} Adicionada com Sucesso!', "concluido")
        return redirect(url_for('paginaTurmas'))
    else:
        os.remove(planilha.filename)
        flash(f'Sua Planinha não foi salva! Verifique os Dados e tente novamente', "erro")
        return redirect(url_for('paginaTurmas'))


#Responsável por pegar a planilha com as informações de cada curso
@App.post("/cadastro_curso")
def cadastrarCurso():
    planilha = request.files["planilha"]
    sheet = request.form["sheet"]

    planilha.save(planilha.filename)
    cadastro_curso = aluno.cadastrar_curso(planilha)

    if cadastro_curso != False:
        os.remove(planilha.filename)
        flash(f'Planilha {planilha.filename} Adicionada com Sucesso!', "concluido")
        return redirect(url_for('paginaTurmas'))
    else:
        os.remove(planilha.filename)
        flash(f'Sua Planinha não foi salva! Verifique os Dados e tente novamente', "erro")
        return redirect(url_for('paginaTurmas'))
    

#Responsável por pegar a planilha com as informações de cada disciplina classificada como da base comum
@App.post("/cadastro_disciplinas_bc")
def cadastrarDisciplinasBC():
    planilha = request.files["planilha"]
    sheet = request.form["sheet"]

    planilha.save(planilha.filename)
    cadastro_disciplinas_bc = aluno.cadastrar_turma_disciplinas_base_comum(planilha)

    if cadastro_disciplinas_bc != False:
        os.remove(planilha.filename)
        flash(f'Planilha {planilha.filename} Adicionada com Sucesso!', "concluido")
        return redirect(url_for('paginaTurmas'))
    else:
        os.remove(planilha.filename)
        flash(f'Sua Planinha não foi salva! Verifique os Dados e tente novamente', "erro")
        return redirect(url_for('paginaTurmas'))


#Responsável por pegar a planilha com as informações de cada disciplina classificada como das trilhas
@App.post("/cadastro_disciplinas_trilha")
def cadastrarDisciplinasTrilha():
    planilha = request.files["planilha"]
    sheet = request.form["sheet"]

    planilha.save(planilha.filename)
    cadastro_disciplinas_trilha = aluno.cadastrar_turma_disciplinas_trilha(planilha, str(sheet))

    if cadastro_disciplinas_trilha != False:
        os.remove(planilha.filename)
        flash(f'Planilha {planilha.filename} Adicionada com Sucesso!', "concluido")
        return redirect(url_for('paginaTurmas'))
    else:
        os.remove(planilha.filename)
        flash(f'Sua Planinha não foi salva! Verifique os Dados e tente novamente', "erro")
        return redirect(url_for('paginaTurmas'))


#Responsável por pegar a planilha com as informações de cada disciplina classificada como das eletivas
@App.post("/cadastro_disciplinas_eletiva")
def cadastrarDisciplinasEletiva():
    planilha = request.files["planilha"]
    sheet = request.form["sheet"]

    planilha.save(planilha.filename)
    cadastro_disciplinas_eletiva = aluno.cadastrar_turma_disciplinas_eletiva(planilha, str(sheet))

    if cadastro_disciplinas_eletiva != False:
        os.remove(planilha.filename)
        flash(f'Planilha {planilha.filename} Adicionada com Sucesso!', "concluido")
        return redirect(url_for('paginaTurmas'))
    else:
        os.remove(planilha.filename)
        flash(f'Sua Planinha não foi salva! Verifique os Dados e tente novamente', "erro")
        return redirect(url_for('paginaTurmas'))


#Responsável por pegar a planilha com as informações de cada disciplina do curso técnico
@App.post("/cadastro_disciplinas_curso")
def cadastrarDisciplinasCurso():
    planilha = request.files["planilha"]
    sheet = request.form["sheet"]

    planilha.save(planilha.filename)
    cadastro_disciplinas_curso = aluno.cadastrar_turma_disciplinas_curso(planilha, str(sheet))

    if cadastro_disciplinas_curso != False:
        os.remove(planilha.filename)
        flash(f'Planilha {planilha.filename} Adicionada com Sucesso!', "concluido")
        return redirect(url_for('paginaTurmas'))
    else:
        os.remove(planilha.filename)
        flash(f'Sua Planinha não foi salva! Verifique os Dados e tente novamente', "erro")
        return redirect(url_for('paginaTurmas'))

#=====================================================================================================================

#Pagina Editar -- Get
@App.get("/editar")
def paginaEditarAluno_get():
    if (verificarLogin(["admin"])):
        id_aluno = request.args.get("id_aluno")
        id_curso = request.args.get("id_curso")
        uptade_aluno = aluno.exibir_aluno(id_aluno, id_curso)
        uptade_curso = aluno.exibir_aluno(id_aluno, id_curso)

        print(id_curso)
        return render_template("pageEditar.html", aluno = uptade_aluno, curso = uptade_curso)
    else:
        return redirect(url_for('paginaLogin_get'))


#INCOMPLETA
#Pagina Editar -- Post
@App.post("/editar")
def paginaEditarAluno_post():
    if (verificarLogin(["admin"])):
        alunos = aluno.listar_alunos("*")

        id_aluno = request.form["id_aluno"]
        nome_aluno = request.form["nome_aluno"]
        nome_pai = request.form["nome_pai"]
        nome_mae = request.form["nome_mae"]
        cpf_aluno = request.form["cpf_aluno"]
        municipio_aluno = request.form["municipio_aluno"]
        estado_aluno = request.form["estado_aluno"]
        nascimento_aluno = request.form["nascimento_aluno"]
        rg_aluno = request.form["rg_aluno"]
        orgao_aluno = request.form["orgao_aluno"]
        turma_aluno = request.form["turma_aluno"]
        nome_curso = request.form["nome_curso"]
        eixo_tecnologico = request.form["eixo_tecnologico"]


        if cpf_aluno != cpf_aluno:
            for aluno in alunos:
             if cpf_aluno == aluno[4]:
                    flash("Esse CPF ja pertence a outro aluno!", "erroEditarAluno")
                    return redirect(url_for('paginaEditarAluno_get', id_aluno = id_aluno))
             elif rg_aluno == aluno[8]:
                    flash("Esse RG ja pertence a outro aluno!", "erroEditarAluno")
                    return redirect(url_for('paginaEditarAluno_get', id_aluno = id_aluno))
        else:
            aluno.editar_aluno(id_aluno, nome_aluno, nome_mae, nome_pai, cpf_aluno, municipio_aluno, estado_aluno, nascimento_aluno, rg_aluno, orgao_aluno, turma_aluno, nome_curso, eixo_tecnologico)
            return redirect(url_for('paginaEditarAluno_get', id__aluno = id_aluno))
        
    else:
        return redirect(url_for('paginaLogin_get'))


#Delete Aluno
@App.get("/delete")
def deletarAluno():
    certificadosCriados = checarCertificadosCriados()
    id_aluno = request.args.get("id_aluno")
    info_aluno = aluno.exibir_aluno(id_aluno)

    for certificado in certificadosCriados:
        if certificado == id_aluno:
            flash(f'Este Aluno tem um Certificado Gerado. Apague o Certificado "{id_aluno} - {info_aluno[1]}" antes de Deletar o Aluno', "erro")
            return redirect(url_for('paginaInicial'))

    aluno.deletar_aluno(id_aluno)
    flash(f'Aluno {info_aluno[1]} Deletado com Sucesso!', "concluido")
    return redirect(url_for('paginaInicial'))


#Gerar Certificado dos Alunos
@App.get("/certificado")
def gerarCertificado():
    id_aluno = request.args.get("id_aluno")

    modelo = pegarModelo()   
    if modelo == None:
        flash("Modelo não Encotrado, Adicione-o na pagina 'Configurar Dados'", "erro")
        return redirect(url_for('paginaInicial'))
    else:
        certificado.gerar_certificado(modelo, id_aluno)
        info_aluno = certificado.exibir_aluno(id_aluno)

        flash(f'Certificado de {info_aluno[1]} Gerado com Sucesso!', "concluido")
        return redirect(url_for('paginaInicial'))


#Gerar os Certificados de Todos os Alunos
@App.get("/gerar_certificado")
def gerarTodosCertificados():   
    seletor = request.args.get("seletor")
    alunos = aluno.listar_alunos(seletor)
    modelo = pegarModelo()
    
    if modelo == None:
        flash("Modelo não Encotrado, Adicione-o na pagina 'Configurar Dados'", "erro")
    else:
        if alunos:
            filename = usuario.GerarTodosCertificados(alunos, modelo)
            flash("Todos os Certificados foram Gerados e Baixados")
            return redirect(url_for('static', filename=f'{filename}.zip'))
        else:
            flash("Adicione Alunos para essa Ação", "erro")
            return redirect(url_for('paginaInicial'))

# END pageHome -------------------------------------------------------------------------------------------------------------

#START pageCadastrarAlunoUnico
@App.get("/cadastrar_aluno_unico")
def paginaCadastrarAluno_get():
    if (verificarLogin(["admin"])):
        return render_template("pageCadastrarAluno.html")
        
    else:
        return redirect(url_for('paginaLogin_get'))


#INCOMPLETA
@App.post("/cadastrar_aluno_unico")
def cadastrarAluno_post():
    try:
        nome_aluno = request.form["nome_aluno"]
        nome_pai = request.form["nome_pai"]
        nome_mae = request.form["nome_mae"]
        cpf_aluno = request.form["cpf_aluno"]
        municipio_aluno = request.form["municipio_aluno"]
        estado_aluno = request.form["estado_aluno"]
        nascimento_aluno = request.form["nascimento_aluno"]
        rg_aluno = request.form["rg_aluno"]
        orgao_aluno = request.form["orgao_aluno"]
        turma_aluno = request.form["turma_aluno"]

        cadastro = aluno.cadastrar_aluno(nome_aluno, nome_mae, nome_pai, cpf_aluno, municipio_aluno, estado_aluno, nascimento_aluno, rg_aluno, orgao_aluno, turma_aluno)
        
        if cadastro:
            flash("Aluno Cadastrado com Sucesso")
            return redirect(url_for('paginaInicial'))
        else:
            flash("Erro ao Cadastrar o Aluno")
            return redirect(url_for('paginaInicial'))
    except:
        flash("Erro ao Cadastrar o Aluno")
    return render_template("pageCadastrarAluno.html")

#END pageCadastrarAlunoUnico


#START pageAjuda------------------------------------------------------------------------------------------------------------------------------------
#Pagina Ajuda
@App.get("/ajuda")
def paginaAjuda():
    if (verificarLogin(["admin"])):
        return render_template("pageAjuda.html")
    else:
        return redirect(url_for('paginaLogin_get'))

#END pageAjuda------------------------------------------------------------------------------------------------------------------------


#START pageConfigurar------------------------------------------------------------------------------------------------------------------------------------
#Baixar Planilha Base
@App.get("/baixar_planilha_base_turmas_alunos")
def baixarPlaninhaTurmasAlunos():
    return redirect(url_for('static', filename='midia/PlanilhaBase_Turmas_Alunos.xlsx'))


@App.get("/baixar_plalinha_base_curso")
def baixarPlaninhaCurso():
    return redirect(url_for('static', filename='midia/PlanilhaBase_Cursos_Técnicos.xlsx'))


@App.get("/baixar_planilha_base_turmas_disciplinas_base_comum")
def baixarPlaninhaTurmasDisciplinasBC():
    return redirect(url_for('static', filename='midia/PlanilhaBase_Turmas_Matérias_Base _Comum.xlsx'))


@App.get("/baixar_planilha_base_turmas_disciplinas_tecnico")
def baixarPlaninhaTurmasDisciplinasTecnico():
    return redirect(url_for('static', filename='midia/PlanilhaBase_Turmas_Matérias_Técnico.xlsx'))


@App.get("/baixar_planilha_base_turmas_disciplinas_trilha")
def baixarPlaninhaTurmasDisciplinasTrilha():
    return redirect(url_for('static', filename='midia/PlanilhaBase_Turmas_Matérias_Trilhas.xlsx'))


@App.get("/baixar_planilha_base_turmas_disciplinas_eletiva")
def baixarPlaninhaTurmasDisciplinasEletiva():
    return redirect(url_for('static', filename='midia/PlanilhaBase_Turmas_Matérias_Eletivas.xlsx'))


#Pagina Configurar Modelo
@App.get("/configurar")
def paginaConfigurar_get():
    if (verificarLogin(["admin"])):
        caminho = "static/midia/Modelo"

        for p, _, files in os.walk(os.path.abspath(caminho)):
            for file in files:
                if file != None:
                    return render_template("pageConfigurar.html", modelo = file)
        else:
            return render_template("pageConfigurar.html", modelo = None)    
    else:
        return redirect(url_for('paginaLogin_get'))

@App.post("/configurar")
def paginaConfigurar_post():
    caminho = "static/midia/Modelo/"
    modelo_novo = request.files["modelo_novo"]
    modelo_antigo = request.form["modelo_antigo"]

    if modelo_antigo == "None":
        modelo_novo.save(caminho + modelo_novo.filename)
        flash("Modelo Cadastrado Com Sucesso!")
        return render_template("pageConfigurar.html")
    else: 
        os.remove(caminho + modelo_antigo)
        modelo_novo.save(caminho + modelo_novo.filename)
        flash("Modelo Cadastrado Com Sucesso!")
        return render_template("pageConfigurar.html")
    
def pegarModelo():
    caminho = "static/midia/Modelo/"
    for p, _, files in os.walk(os.path.abspath(caminho)):
        for file in files:
            if file != None:
                modelo = caminho + file
                return modelo
    
            
#END pageConfigurar------------------------------------------------------------------------------------------------------------------------


#START pageCadastroUsuario--------------------------------------------------------------------------------------------------------------------
# Pagina Cadastro -- Get
@App.get("/cadastrar_usuario")
def paginaCadastrarUsuario_get():
    if (verificarLogin(["admin"])):
        usuarios = usuario.exibir_usuarios()
        return render_template("pageCadastroUsuario.html", usuarios_cadastrados = usuarios)
    else:
        return redirect(url_for('paginaLogin_get'))
    

#Pagina Cadastro - Deletar Usuario
@App.route("/deletar_usuario")
def deletarUsuario():
    id_usuario = request.args.get("id_usuario")
    usuario.deletar_usuario(id_usuario)
    flash("Usuário Deletado Com Sucesso", "deleteUsuario")
    return redirect(url_for('paginaCadastrarUsuario_post'))


# Pagina Cadastro -- Post
@App.post("/cadastrar_usuario")
def paginaCadastrarUsuario_post():
    login = request.form["login"]
    senha = request.form["senha"]

    login_upper = login.upper()

    cadastro_usuario = usuario.cadastrar_usuario(login_upper, senha)

    if (cadastro_usuario == True):
        flash("Usuario Cadastrado!","CadastroUsuario") #Flash para mensagem de certo
        return redirect(url_for('paginaCadastrarUsuario_get'))
    else:
        flash('Usuario ou Senha ja Existentes!', "CadastroUsuario") #Flash para mensagem de erro
        return redirect(url_for('paginaCadastrarUsuario_get'))

#END pageCadastroUsuario---------------------------------------------------------------------------------------------------------------


#START pageCertificados------------------------------------------------------------------------------------------------------------------------------------
@App.get("/certificados")
def paginaCertificados():
    if (verificarLogin(["admin"])):
        certificados = checarCertificadosCriados()
        certificados_alunos =  certificado.certificados(certificados)
        paginacao_pp = paginacao(certificados_alunos)
        return render_template("pageCertificado.html", certificados = paginacao_pp[0],
                               total_pages = paginacao_pp[1],
                               page = paginacao_pp[2])
    else:
        return redirect(url_for('paginaLogin_get'))


@App.get("/baixar_certificado")
def baixarCertificado():
    id_aluno = request.args.get("id_aluno")
    nome_certificado = request.args.get("nome_certificado")
    info_aluno =  aluno.exibir_aluno(id_aluno)

    certificado_aluno = "Certificados/" + id_aluno + "-" + nome_certificado + ".docx"

    return redirect(url_for('static', filename= certificado_aluno))


@App.get("/deletar_certificado")
def deletarCertificado():
    id_aluno = request.args.get("id_aluno")
    nome_certificado = request.args.get("nome_certificado")

    pastaCertificado = "static/Certificados/" + id_aluno + "-" + nome_certificado + ".docx"

    os.remove(pastaCertificado)
    flash("Certificado Deletado com Sucesso!")
    return redirect(url_for('paginaCertificados'))


@App.get("/deletar_todos_certifcados")
def deletarTodosCertificados():
    certificados = checarCertificadosCriados()
    if certificados != []:
        try:
            for certificado in certificados:
                aluno = aluno.exibir_aluno(certificado)
        
                pastaCertificado = "static/Certificados/" + certificado + "-" + aluno[1] + ".docx"

                os.remove(pastaCertificado)
            flash("Todos Certificados Deleteados Com Sucesso!", "concluido") 
        except:
            flash("Erro ao Deletar os Certificados", "erro")
        finally:
            return redirect(url_for('paginaCertificados'))
    else:
        flash("Nenhum Certificado Gerado!", "erro")
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
        login_upper = request.form["login"].upper()
        acesso = usuario.login_usuario(login_upper, request.form["senha"])
        if(acesso != None):
            if (login_upper == acesso[1] and request.form["senha"] == acesso[2]):
                session['logado'] = True
                session['nivel'] = "admin"
                session['usuario'] = acesso[1]
                return redirect(url_for('paginaInicial'))
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

#Verificação dos Certificados Criados
def checarCertificadosCriados():
    certificados_criados = []
    caminho = "static/Certificados"

    for p, _, files in os.walk(os.path.abspath(caminho)):
        for file in files:
            id_certificado = (file[:-5].split('-'))
            certificados_criados.append(id_certificado[0])

    return certificados_criados
           

#Logout do Usuario
@App.route("/logout")
def logout():
    session.clear()
    flash("Desconectado Com Sucesso", "Logout")
    return redirect("/inicio")


# paginacao do Site
def paginacao(lista_alunos):
    per_page = 10
    total_pages = (len(lista_alunos) + per_page) // per_page
    page = request.args.get('page', 1, type=int)

    if page > total_pages:
        page = total_pages - 1

    start = (page - 1) * per_page
    end = start + per_page 
    
    items_on_page = lista_alunos[start:end]
    return items_on_page, total_pages, page


App.run(debug=True)