from flask import Flask
from utils.db import db
from services.estudiante import estudiantes
from services.test import tests
from services.area import areas
from services.pregunta import preguntas
from services.respuesta import respuestas  # Importar el blueprint de Respuestas
from services.test_amasc import test_amasc_bp
from services.test_beck import test_beck_bp
from services.test_zung import test_zung_bp
from config import DATABASE_CONNECTION
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

# Inicializar SQLAlchemy
db.init_app(app)

# Registrar Blueprints
app.register_blueprint(estudiantes)
app.register_blueprint(tests)
app.register_blueprint(areas)
app.register_blueprint(preguntas)
app.register_blueprint(respuestas)  # Registrar el blueprint de Respuestas
app.register_blueprint(test_amasc_bp)
app.register_blueprint(test_beck_bp)
app.register_blueprint(test_zung_bp)

with app.app_context():
    db.create_all()

#################### PARA PROBAR SI HAY CONEXIÓN
@app.route('/check_db')
def check_db():
    try:
        with db.engine.connect() as connection:
            result = connection.execute(text('SELECT 1'))
            return 'Database connection successful!', 200
    except Exception as e:
        return str(e), 500
##########################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
