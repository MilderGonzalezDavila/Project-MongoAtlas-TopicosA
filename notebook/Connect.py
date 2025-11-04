from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

MONGODB_URI = os.getenv('MONGODV_URI_ATLAS')
DB_NAME_ATLAS = os.getenv('MONGODB_DATA')

try:
    client = MongoClient(MONGODB_URI)
    db = client[DB_NAME_ATLAS]
    print("Conexión exitosa correctamente")
except errors.ServerSelectionTimeoutError as e:
    print('No se pudo contectar', e)
except errors.OperationFailure as e:
    print('Erro de auntenticacion', e)
except Exception as e:
    print('No se que pasó')

