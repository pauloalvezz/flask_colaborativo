# Exemplo de rota personalizada

def inicializar(app):
    @app.route('/exemplo')
    def rota_exemplo():
        return '<h1>Olá, esta é a rota de exemplo!</h1>'