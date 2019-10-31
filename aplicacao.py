from flask import Flask, render_template #devolve arq html especifico
from curso import Curso

app = Flask(__name__)  #variavel global
from controles import *



if __name__ == "__main__":
    app.run(debug=True) # modo testando



