from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_image(file_path):
    key = get_random_bytes(32)

    with open(file_path, "rb") as f:
        data = f.read()

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    encrypted_data = cipher.iv + ciphertext

    return encrypted_data, key