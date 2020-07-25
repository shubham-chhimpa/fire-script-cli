import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import argparse
import os

# initialize the parser
parser = argparse.ArgumentParser(description="Script to update all documents with new field in a collection of "
                                             "Firebase Firestore Database ")

# add arguments
parser.add_argument("-k", "--key", help="Google Cloud Service Key File(JSON) path")
parser.add_argument("-c", "--collection", help="Collection Name")
parser.add_argument("-f", "--field", help="Field Name")
parser.add_argument("-v", "--value", help="Field Value")

# parse the arguments
args = parser.parse_args()

# adding field to firestore collection logic

try:
    key_path = os.path.normpath(args.key)
except ValueError:
    print("enter valid key path")

try:
    collection: str = args.collection
except ValueError:
    print("enter valid collection name")

try:
    field_name: str = args.field
except ValueError:
    print("enter valid field name")

try:
    field_value = args.value
except ValueError:
    print("enter valid key path")

# Use a service account
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection(collection)
docs = collection_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    collection_ref.document(doc.id).update(
        {
            field_name: field_value
        }
    )
