from tinydb12 import runningdb as DB

# Example usage
user_id = "123"  # Replace this with the actual user ID

# Change status to "running" for the provided user ID
DB.change_status("free", user_id)

# Check if the database is in use and get the user ID if it is
in_use, using_user_id = DB.is_database_in_use()
if in_use:
    print(f"Database is in use by user {using_user_id}")
else:
    print("Database is free")

# Get the user ID of the user currently using the database
current_user_id = DB.get_user_id()
if current_user_id:
    print(f"The database is being used by user {current_user_id}")
else:
    print("No user is currently using the database ", current_user_id )
