from flask import Flask, render_template
import os
from rotas import registrar_rotas

app = Flask(__name__)
registrar_rotas(app)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)