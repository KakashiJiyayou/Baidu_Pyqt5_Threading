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


def insert_into_dir_list(client, path, created_by, sku_filter):
    db = client.get_database("bypy")
    collection = db.dir_list

    document = {
        "path": path,
        "created_at": None,
        "updated_at": None,
        "created_by": created_by,
        "updated_by": None,
        "sku_filter": sku_filter
    }

    try:
        result = collection.insert_one(document)
        print("Document inserted with ID:", result.inserted_id)
    except Exception as e:
        print("Error inserting document:", e)
        traceback.print_exc()


# Example usage
uri = "mongodb+srv://rafibapi:MongoDb123@forresearch.9dw6wne.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = connect_to_mongodb(uri)

if client:
    # Perform insertion
    insert_into_dir_list(client, "main.py", "admin", "menu.menu.menu")

    # Close the MongoDB connection
    close_mongodb_connection(client)
