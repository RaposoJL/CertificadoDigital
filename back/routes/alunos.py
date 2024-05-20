from flask import Blueprint, render_template

aluno_route = Blueprint('cliente', __name__)

''''Listar todos os alunos'''
@aluno_route.route('/')
def listar_alunos():
    return render_template('lista_alunos')


@aluno_route.route('/', methods=["POST"])
def insertir_aluno():
    return render_template('inserir_alunos')

'''Insertir aluno'''
@aluno_route.route('/new')
def form_aluno():
    return render_template('form_alunos')

@aluno_route.route('/<int:cliente_id>')
def detalhe_aluno(cliente_id):
    return render_template('detalhe_alunos')

@aluno_route.route('/<int:cliente_id>/edit')
def edit_aluno(cliente_id):
    return render_template('edit_alunos')

@aluno_route.route('/<int:cliente_id>/update', methods=['PUT'])
def update_aluno(cliente_id):
    pass

@aluno_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def delete_aluno(cliente_id):
    pass