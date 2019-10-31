from curso import Curso
from flask import render_template
from aplicacao import app



@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo="Faculdade de Tecnologia",
        cursos= busca_cursos()
    )
        
        

@app.route('/historia')
def historia():
    return render_template (
        'historia.html',
        cursos = busca_cursos()
        
        )