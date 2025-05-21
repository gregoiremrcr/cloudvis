from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
    client.server_info()  # Teste la connexion, ça lève une exception si ça rate
    print("Connexion MongoDB réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
