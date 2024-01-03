from models.connections_options.connection import DBConnectionHandler


db_handle = DBConnectionHandler()
conn1 = db_handle.get_db_connection()
print(conn1)


db_handle.connect_to_db()
conn2 = db_handle.get_db_connection()
print(conn2)

collection = conn2.get_collection("minhaCollection")
collection.insert_one({
    "Estou":"Inserindo",
    "Numeros":[123, 456, 789]
})
