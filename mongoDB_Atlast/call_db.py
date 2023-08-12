from mongoDB_Atlast.mongo_utils import MongoDBUtils

# Create an instance
mongo_utils = MongoDBUtils()

# Establish connection
client = mongo_utils.connect()
if client:
    print ( "working")

# Close the connection
mongo_utils.close_connection()