import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Initialize the database
db = client["octofit_db"]

# Check if a collection exists before creating it
def create_collection_if_not_exists(db, collection_name):
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)

# Users collection with unique email index
db.users.create_index("email", unique=True)

# Teams collection
create_collection_if_not_exists(db, "teams")

# Activity collection
create_collection_if_not_exists(db, "activity")

# Leaderboard collection
create_collection_if_not_exists(db, "leaderboard")

# Workouts collection
create_collection_if_not_exists(db, "workouts")

print("Database and collections initialized successfully.")