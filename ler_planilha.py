import openpyxl

# carregando arquivos
book = openpyxl.load_workbook('AlunosTurmas.xlsx')
# Selecionando uma pagina
Alunos_page = book['1 - TDS3IN-A']

Matricula = Alunos_page['A']
Nome = Alunos_page['B']
CPF = Alunos_page['C']
RG = Alunos_page['D']
Naturalidade = Alunos_page['E']
Orgao_Expeditor = Alunos_page['F']
Nome_pai = Alunos_page['G']
Nome_mae = Alunos_page['H']
Curso = Alunos_page['I']

aluno = []


for celula in Matricula:
    aluno = celula.value
    print(aluno)
