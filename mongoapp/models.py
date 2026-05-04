from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['CrudMongo']
vehiculos_collection = db['vehiculos']