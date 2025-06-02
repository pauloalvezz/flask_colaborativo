# Exemplo de rota personalizada

def inicializar(app):
    @app.route('/victor')
    def rota_victor():
        return '<h1>Olá, esta é a rota de Victor!</h1>'