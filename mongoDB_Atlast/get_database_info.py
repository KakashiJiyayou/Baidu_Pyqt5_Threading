from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://rafibapi:MongoDb123@forresearch.9dw6wne.mongodb.net/?retryWrites=true&w=majority"
# uri = "mongodb+srv://rafibapi:MongoDb123@forresearch.9dw6wne.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# database variable
db = client.get_database("bypy")

# Access the "dir_list" collection
collection = db.dir_list

# count rows or document in dir_list
count_dir_list = collection.count_documents({})
print (count_dir_list)

client.close()