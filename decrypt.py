from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_image(encrypted_data, key, output_file):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    original = unpad(cipher.decrypt(ciphertext), AES.block_size)

    with open(output_file, "wb") as f:
        f.write(original)