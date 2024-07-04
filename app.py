import firebase_admin
from firebase_admin import credentials, firestore

# Configura la credencial de administración del proyecto original
cred_original = credentials.Certificate('path/to/original/serviceAccountKey.json')
firebase_admin.initialize_app(cred_original)
db_original = firestore.client()

# Configura la credencial de administración del nuevo proyecto
cred_new = credentials.Certificate('path/to/new/serviceAccountKey.json')
app_new = firebase_admin.initialize_app(cred_new, name='new_project')
db_new = firestore.client(app_new)

# Collections to migrate
tables = [
    'client',
    'company'
]

for table in tables:
    docs = db_original.collection(table).stream()
    for doc in docs:
        doc_dict = doc.to_dict()
        db_new.collection(table).document(doc.id).set(doc_dict)
        print(f'Migrated document {doc.id} in table {table}')

print("Migration complete.")
