"""
here we'll
activate our app instance
"""

from app import app, blueprint

if __name__ == '__main__':
    app.register_blueprint(blueprint)
    app.run()
