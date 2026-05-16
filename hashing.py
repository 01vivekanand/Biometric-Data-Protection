import hashlib

def hash_id(patient_id):
    return hashlib.sha256(patient_id.encode()).hexdigest()