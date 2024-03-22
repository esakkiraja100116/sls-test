# mongo_operations.py
import os
from pymongo import MongoClient

# Load MongoDB URI from environment variables
MONGO_URI = os.getenv('MONGO_URI')

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client.test_database # Use your database name
collection = db.nodes # Use your collection name

def lambda_handler(event):
    http_method = event['httpMethod']
    if http_method == 'POST':
        node_data = event['body']
        return createNode(node_data)
    elif http_method == 'PUT':
        node_id = event['pathParameters']['id']
        update_data = event['body']
        return updateNode(node_id, update_data)
    elif http_method == 'DELETE':
        node_id = event['pathParameters']['id']
        return deleteNode(node_id)
    elif http_method == 'GET':
        node_id = event['pathParameters']['id']
        return getNode(node_id)
    else:
        return {
            'statusCode': 400,
            'body': 'Invalid request method'
        }

def createNode(node_data):
    result = collection.insert_one(node_data)
    return { 'statusCode': 201 }

def updateNode(node_id, update_data):
    result = collection.update_one({"_id": node_id}, {"$set": update_data})
    return {
        'statusCode': 200,
        'body': str(result.modified_count)
    }

def deleteNode(node_id):
    result = collection.delete_one({"_id": node_id})
    return {
        'statusCode': 200,
        'body': str(result.deleted_count)
    }

def getNode(node_id):
    node = collection.find_one({"_id": node_id})
    return {
        'statusCode': 200,
        'body': str(node)
    }