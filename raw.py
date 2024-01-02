from dotenv import load_dotenv
import os 

load_dotenv()

from pymongo import MongoClient

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

connection_string = f"mongodb://{username}:{password}@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["meuBanco"]


collection = db_connection.get_collection("minhaCollection")

search_filter = {"estou": "aqui"}

response = collection.find(search_filter)


print(response)


for registry in response: print(registry)

collection.insert_one({
    "Estou":"Inserindo",
    "Numeros":[123, 456, 789]
})