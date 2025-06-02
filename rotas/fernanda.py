def inicializar(app):
    @app.route('/fernandallobao')
    def rota_exemplo():
        return '<h1>Olá, esta é a rota da Fernanda!</h1>'