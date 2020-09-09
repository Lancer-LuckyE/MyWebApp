from datetime import timedelta


def config(app):
    app.config['JWT_SECRET_KEY'] = 'secret'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1.0)
    return app.config
