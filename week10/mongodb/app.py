from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://cluster0.bydnl.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(
    uri,
    tls=True,
    tlsCertificateKeyFile="X509-cert-76227297056933959.pem",
    server_api=ServerApi("1"),
)


db = client["brevetsdb"]
collection = db["brevet_info"]
doc_count = collection.count_documents({})
print(f"Database contains {doc_count} documents")

# Print all documents in the collection
for doc in collection.find():
    print(doc)
