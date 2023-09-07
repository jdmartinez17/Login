from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://martinezvegajuandavid3:1217JD@ambiente.ytgxj1u.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

# definimos el método de conexión
def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["Login"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db