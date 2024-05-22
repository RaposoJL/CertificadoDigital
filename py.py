import openpyxl

class MyClass:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

p1 = MyClass("Arnaldo", 20)
print(p1.nome)



# carregando arquivos
book = openpyxl.load_workbook('AlunosTurmas.xlsx')
# Selecionando uma pagina
Alunos_page = book['1 - TDS3IN-A']
# Imprimindo nomes das linhas~
Matricula = Alunos_page['A']
Nome = Alunos_page['B']
CPF = Alunos_page['C']
RG = Alunos_page['D']
Naturalidade = Alunos_page['E']
Orgao_Expeditor = Alunos_page['F']
Nome_pai = Alunos_page['G']
Nome_mae = Alunos_page['H']
Curso = Alunos_page['I']


contador = 0
colunas = 8
colunasmax = 8
while contador < colunasmax:
    for rows in Alunos_page.iter_rows(min_row=contador, max_row=colunasmax):
        for cell in rows:
            print(cell.value) 
    contador = contador + 1
    colunas = colunas + 1
