from dotenv import load_dotenv
import os 

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

mongo_db_infos ={
    "HOST": "localhost",
    "PORT": "27017",
    'USERNAME': f'{username}',
    'PASSWORD': f'{password}',
    'DB_NAME': 'meuBanco'
}