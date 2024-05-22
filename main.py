from flask import Flask, render_template
from routes.home import home_route
from  routes.alunos import aluno_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(aluno_route, url_prefix='/alunos')