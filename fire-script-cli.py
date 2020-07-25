import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import argparse
import os

# initialize the parser
parser = argparse.ArgumentParser(description="CLI to update all documents with new field in a collection of "
                                             "Firebase Firestore Database ")

# add arguments
parser.add_argument("-k", "--key", help="Google Cloud Service Key File(JSON) path")
parser.add_argument("-c", "--collection", help="Collection Name")
parser.add_argument("-f", "--field", help="Field Name")
parser.add_argument("-v", "--value", help="Field Value")

# parsing the arguments
args = parser.parse_args()

key_path: str = args.key
collection: str = args.collection
field_name: str = args.field
field_value: any = args.value

# checking the credentials
cred = credentials.Certificate(os.path.normpath(key_path))
firebase_admin.initialize_app(cred)

# initializing the database
db = firestore.client()

# getting the collection ref
collection_ref = db.collection(collection)
docs = collection_ref.stream()

# adding the field to all the docs iteratively
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    collection_ref.document(doc.id).update(
        {
            field_name: field_value
        }
    )
