from pymongo.mongo_client import MongoClient
import traceback


def connect_to_mongodb(uri):
    client = None
    try:
        client = MongoClient(uri)
        client.admin.command('ping')
        print("Connected to MongoDB")
    except Exception as e:
        print("Error connecting to MongoDB:", e)
        traceback.print_exc()
    return client


def close_mongodb_connection(client):
    try:
        if client:
            client.close()
            print("Connection to MongoDB closed")
    except Exception as e:
        print("Error closing MongoDB connection:", e)
        traceback.print_exc()


def view_dir_list_documents(client):
    db = client.get_database("bypy")
    collection = db.dir_list

    try:
        documents = collection.find()
        for document in documents:
            print(document)
    except Exception as e:
        print("Error viewing documents:", e)
        traceback.print_exc()


# Example usage
uri = "mongodb+srv://rafibapi:MongoDb123@forresearch.9dw6wne.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = connect_to_mongodb(uri)

if client:
    # View documents in the dir_list collection
    view_dir_list_documents(client)

    # Close the MongoDB connection
    close_mongodb_connection(client)