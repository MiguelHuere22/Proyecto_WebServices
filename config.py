from dotenv import load_dotenv
import os

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

user = os.getenv('USER')
pwd = os.getenv('PASSWORD')
host = os.getenv('HOST')
database = os.getenv('DATABASE')
port = os.getenv('PORT')

# Imprimir las variables para verificar
print(f"USER: {user}")
print(f"PASSWORD: {pwd}")
print(f"DATABASE: {database}")
print(f"HOST: {host}")
print(f"PORT: {port}")

DATABASE_CONNECTION = f'postgresql://{user}:{pwd}@{host}:{port}/{database}'
