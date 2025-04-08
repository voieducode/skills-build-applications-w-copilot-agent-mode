from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

def test_mongo_connection():
    try:
        # Update these credentials with your MongoDB details
        client = MongoClient(
            host="localhost",
            port=27017,
            username="thundergod",
            password="thundergodpassword",
            authSource="admin",
            authMechanism="SCRAM-SHA-1",
        )

        # Attempt to connect and fetch server info
        client.admin.command("ping")
        print("MongoDB connection successful!")
    except ConnectionFailure:
        print("Failed to connect to MongoDB. Please check the host and port.")
    except OperationFailure as e:
        print(f"Authentication failed: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    test_mongo_connection()
