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
from sqlalchemy import text
from dotenv import load_dotenv
import os
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('USER')}:{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DATABASE')}"

# Inicializar SQLAlchemy
logging.info("Initializing database connection")
db.init_app(app)

# Registrar Blueprints
logging.info("Registering blueprints")
app.register_blueprint(estudiantes)
app.register_blueprint(tests)
app.register_blueprint(areas)
app.register_blueprint(preguntas)
app.register_blueprint(respuestas)  # Registrar el blueprint de Respuestas
app.register_blueprint(test_amasc_bp)
app.register_blueprint(test_beck_bp)
app.register_blueprint(test_zung_bp)

with app.app_context():
    logging.info("Creating all database tables")
    db.create_all()

#################### PARA PROBAR SI HAY CONEXIÓN
@app.route('/check_db')
def check_db():
    try:
        logging.info("Checking database connection")
        with db.engine.connect() as connection:
            result = connection.execute(text('SELECT 1'))
            return 'Database connection successful!', 200
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        return str(e), 500
##########################################

if __name__ == '__main__':
    logging.info("Starting Flask application")
    app.run(host='0.0.0.0', port=5000)
