import json
from pymongo import MongoClient
import traceback
import datetime

# Function to read MongoDB credentials from db_credential.json
def read_db_credentials(filename):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print("Error reading credentials:", e)
        traceback.print_exc()
        return None

# Function to establish connection
def establish_connection(credentials):
    try:
        if credentials:
            uri = f"mongodb+srv://{credentials['username']}:{credentials['password']}@{credentials['cluster_uri']}/?retryWrites=true&w=majority"
            client = MongoClient(uri)
            return client
        else:
            return None
    except Exception as e:
        print("Error establishing connection:", e)
        traceback.print_exc()
        return None

# Function to close connection
def close_connection(client):
    try:
        client.close()
        print("Connection closed.")
    except Exception as e:
        print("Error closing connection:", e)
        traceback.print_exc()

# Function to get current timestamp in the desired format
def get_current_timestamp():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time

# Function to insert into dir_list collection
def insert_into_dir_list(client, path, created_by, sku_filter):
    try:
        db = client.get_database("bypy")
        collection = db.dir_list

        document = {
            "path": path,
            "created_at": get_current_timestamp(),
            "updated_at": None,
            "created_by": created_by,
            "updated_by": None,
            "sku_filter": sku_filter
        }

        collection.insert_one(document)
        print("Document inserted successfully.")
    except Exception as e:
        print("Error while inserting document:", e)
        traceback.print_exc()

# Usage example
try:
    credentials = read_db_credentials("db_credential.json")
    if credentials:
        client = establish_connection(credentials)
        if client:
            insert_into_dir_list(client, "path/to/document", "admin", "menu.menu.menu")
except Exception as e:
    traceback.print_exc()
finally:
    if client:
        close_connection(client)