import json
import datetime
from pymongo import MongoClient

class MongoDBUtils:
    def __init__(self, file_path):
        self.uri = self.construct_uri(file_path)
        self.client = None
        self.db = None
        self.collection = None

    @staticmethod
    def construct_uri(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                username = data.get("username")
                password = data.get("password")
                cluster_uri = data.get("cluster_uri")
                return f"mongodb+srv://{username}:{password}@{cluster_uri}/?retryWrites=true&w=majority"
        except Exception as e:
            print("Error constructing URI:", e)
            return None

    def connect(self):
        username, password, cluster_uri = self.read_credentials()
        if username and password and cluster_uri:
            try:
                uri = f"mongodb+srv://{username}:{password}@{cluster_uri}/?retryWrites=true&w=majority"
                self.client = MongoClient(uri)
                self.ping_server()
                return self.client
            except Exception as e:
                print("Error establishing connection:", e)
                return None
        else:
            print("Credentials not provided.")
            return None

    def close_connection(self):
        try:
            self.client.close()
            print("Connection closed.")
        except Exception as e:
            print("Error closing connection:", e)

    def ping_server(self):
        if self.client is None:
            raise ValueError("Connection not established")

        try:
            self.client.admin.command('ping')
            print("Pinged the server. Connection is active.")
        except Exception as e:
            print("Error pinging the server:", e)
            self.close_connection()