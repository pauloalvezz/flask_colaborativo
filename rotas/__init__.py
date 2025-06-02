# Este arquivo irá importar e registrar todas as rotas personalizadas
import os
import importlib

def registrar_rotas(app):
    caminho_rotas = os.path.dirname(__file__)
    for nome_arquivo in os.listdir(caminho_rotas):
        if nome_arquivo.endswith('.py') and nome_arquivo != '__init__.py':
            modulo = f'rotas.{nome_arquivo[:-3]}'
            importlib.import_module(modulo).inicializar(app)