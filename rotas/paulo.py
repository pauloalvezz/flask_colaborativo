def inicializar(app):
    @app.route('/pauloalvezz')
    def rota_paulo():
        return '<h1>Olá, esta é a rota de Paulo!</h1>'