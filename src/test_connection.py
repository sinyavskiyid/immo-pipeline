import os 
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGODB_URI"))
print("URI:", os.getenv("MONGODB_URI"))
db = client["immo"]
ventes = db["ventes_test"]

ventes.insert_many([
    {"ville" : "Nice", "prix": 385000, "surface" : 62, "biens" : [{"type" : "Appartament"}, {"type" : "Cave"}]},
    {"ville": "Nice",   "prix": 520000, "surface": 80},
    {"ville": "Antibes","prix": 410000, "surface": 55, "vue_mer": True},
])

print(client.list_database_names())