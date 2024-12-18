import os
import pyaes


def decrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    new_file_path = file_path.replace(".ransomwaretroll", "")
    with open(new_file_path, "wb") as new_file:
        new_file.write(decrypt_data)
    
    os.remove(file_path)
directory_path = "."
key = b"testeransomwares"

for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith(".ransomwaretroll"):
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)