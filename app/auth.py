import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    cred = credentials.Certificate('techathon24-106b3-firebase-adminsdk-ecjpy-5aa2cc6fa2.json')
    firebase_admin.initialize_app(cred)
else:
    print("[!] Firebase SDK is already initialized")
db = firestore.client()



def signup(name, email, password):
    # Create a new user
    try:
        new_city_ref = db.collection("users").document()
        new_city_ref.set({
            "name": name,
            "email": email,
            "password": password
        })
        return 1
    except:
        return 0


def login(email, password):
    # Check if the user exists
    users_ref = db.collection("users")
    query = users_ref.where("email", "==", email).where("password", "==", password).stream()
    try:
        for doc in query:
            doc_dict = doc.to_dict()
            return [1, doc_dict.get("name")]
    except Exception as e:
        print(e)
    return [0, ""]