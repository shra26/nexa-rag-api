import chromadb
import os

client = chromadb.PersistentClient(path = "./db")
collection = client.get_or_create_collection("docs")

#clear existing documents is any
existing_ids = collection.get()["ids"]
if existing_ids:
    collection.delete(ids=existing_ids)

#embed all files in docs/ folder
for filename in os.listdir("docs"):
    if filename.endswith(".txt"):
        with open(f"docs/{filename}", "r") as f:
            text = f.read()
            collection.add(documents=[text], ids=[filename])
print("Re-embedding complete all documents in docs/ folder in Chroma")