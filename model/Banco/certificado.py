import string
import model.Banco.conexao as conexao
import locale
from datetime import datetime
from docx import Document
import os 
import shutil

#Função que identifica a data de emissão do certificado, guardando ela no banco de dados
def data_hoje(data_emissao):
    try:
        hoje = datetime.now()
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
        data_marcada = hoje.strftime('%d de %B de %Y')

        for data in data_marcada:
            conexao_bd = conexao.iniciar_conexao()
            cursor_bd = conexao_bd.cursor()
            marcar = "INSERT INTO certificado (data_emissao) VALUES (%s);"
            parametros = (data_emissao) 
            cursor_bd.execute(marcar, parametros)
            conexao_bd.commit()
            cursor_bd.close()
            conexao_bd.close()
        return True
    except:
        return False
    

#Função responsável por gerar somente um certificado
def gerar_certificado(documento, id_aluno):
    conexao_bd = conexao.iniciar_conexao()
    query = "SELECT * FROM aluno WHERE id = " + str(id_aluno) +";"
    cursor_bd = conexao_bd.cursor()

    cursor_bd.execute(query)
    info_aluno = cursor_bd.fetchone()
    cursor_bd.close()
    conexao_bd.close()

    print(info_aluno)
    doc = Document(documento)

    substituicoes = {
        '#nome_completo#':  info_aluno[1],
        '#nome_mae#':  info_aluno[2],
        '#nome_pai#':  info_aluno[3],
        '#municipio#':  info_aluno[5],
        '#estado#':  info_aluno[6],
        '#data_nascimento#':  info_aluno[7],
        '#rg#':  info_aluno[8],
        '#orgao_expedidor#':  info_aluno[9],
        '#cpf#':  info_aluno[4]
    }

    def substituicao_em_runs(par, substituicoes):
        texto_total = "".join(run.text for run in par.runs)
        alterado = False

        for chave, valor in substituicoes.items():
            if chave in texto_total:
                texto_total = texto_total.replace(chave, valor)
                alterado = True

        if alterado:
            base_run = par.runs[0] if par.runs else par.add_run()

            for i in range(len(par.runs) - 1, -1, -1):
                par._element.remove(par.runs[i]._element)

            novo_run = par.add_run(texto_total)
            novo_run.bold = base_run.bold
            novo_run.italic = base_run.italic
            novo_run.underline = base_run.underline

            if base_run.font:
                if base_run.font.name:
                    novo_run.font.name = base_run.font.name
                if base_run.font.size:
                    novo_run.font.size = base_run.font.size
                if base_run.font.color and base_run.font.color.rgb:
                    novo_run.font.color.rgb = base_run.font.color.rgb

    for par in doc.paragraphs:
        substituicao_em_runs(par, substituicoes)

    for tabela in doc.tables:
        for linha in tabela.rows:
            for celula in linha.cells:
                for par in celula.paragraphs:
                    substituicao_em_runs(par, substituicoes)


    pasta_certificados = os.path.abspath("static/Certificado/" + str(info_aluno[0]) + "-" + info_aluno[1] +".docx")
    doc.save(pasta_certificados)


#INCOMPLETA
#Função responsável por gerar todos os certificados
def gerar_todos_certificados(alunos, documento):
    for aluno in alunos:
        gerar_certificado(documento, aluno[0])
    
    shutil.make_archive("static/Certificado", 'zip', "static/Certificados/")

    return "Certificado"


#Função responsável por realizar a busca por aluno
def pesquisar_aluno(nome_completo):
    conexao_bd = conexao.iniciar_conexao()
    cursor_bd = conexao_bd.cursor()

    cadastrar = f'SELECT * FROM aluno WHERE nome_completo LIKE "{nome_completo}%"'

    cursor_bd.execute(cadastrar)
    info_aluno = cursor_bd.fetchall()
    cursor_bd.close()
    conexao_bd.close()
    return info_aluno


#Função responsável por exibir certificados que já foram criados
def certificados(certificados_criados):
    lista = []
    conexao_bd = conexao.iniciar_conexao()
    cursor_bd = conexao_bd.cursor()
    
    for id_certificado in certificados_criados:
        query = "SELECT * FROM certificado WHERE id = " + str(id_certificado)
        cursor_bd.execute(query)
        lista.append(cursor_bd.fetchone())

    cursor_bd.close()
    conexao_bd.close()
    return lista