from capture import capture_image
from hashing import hash_id
from encrypt import encrypt_image
from database import insert_data
from decrypt import decrypt_image

# Capture image
capture_image("scan.jpg")

# Hash patient ID
patient_id = input("Enter patient ID: ")
patient_hash = hash_id(patient_id)

# Encrypt image
encrypted_data, key = encrypt_image("scan.jpg")

#  Store in DB
insert_data(patient_hash, encrypted_data)
print("Data stored in MySQL")

#  Decrypt (for demo)
decrypt_image(encrypted_data, key)