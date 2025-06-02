# Exemplo de rota personalizada

def inicializar(app):
    @app.route('/caio')
    def rota_caio():
        return '<h1>Olá, esta é a rota de Caio Harry!</h1>'