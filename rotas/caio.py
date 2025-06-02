# Exemplo de rota personalizada

def inicializar(app):
    @app.route('/Caio_Harrys')
    def rota_Caio_Harrys():
        return '<h1>Olá, esta é a rota de Caio Harry!</h1>'