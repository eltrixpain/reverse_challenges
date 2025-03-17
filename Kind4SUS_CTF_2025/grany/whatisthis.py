import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

KEY = "8f149350416bf5a318c91a4072b4c44fe32ec03d5571412ab0dcfc6cb366574e"
FLAG = "3vQmUeUhdaV39wLvJf2OjwFLnUfx4KhGWcx/gyOnlX4lVIsRf6lAeQCCt7rp4fsCZ7iuVyfW09G7dbNEn8+MEuWzG1HbUTyILGzFGHUw6xo="

class Cipher:
    def encrypt(self, plainText, key):
        iv = os.urandom(16) 
        privateKey = hashlib.sha256(key.encode("utf-8")).digest() 
        cipher = AES.new(privateKey, AES.MODE_CBC, iv)
        encryptedBytes = cipher.encrypt(pad(plainText.encode(), AES.block_size))  
        return base64.b64encode(iv + encryptedBytes).decode()

    def decrypt(self, encrypted, key):
        encryptedData = base64.b64decode(encrypted) 
        iv = encryptedData[:16] 
        privateKey = hashlib.sha256(key.encode("utf-8")).digest()  
        cipher = AES.new(privateKey, AES.MODE_CBC, iv) 
        try:
            decryptedBytes = unpad(cipher.decrypt(encryptedData[16:]), AES.block_size)  
        except:
            exit("Decryption error")
        return decryptedBytes.decode()



pwd = input("\nI swear there's nothing in here!\nGranny's super-secret secret:   ")
h = hashlib.new('sha256')
h.update(pwd.lower().encode())
if h.hexdigest() == KEY:
    cipher = Cipher()
    print("\nI always knew you were the smartest grandchild!")
    print(cipher.decrypt(FLAG,pwd.lower()))
else:
    print("\nI told you, but you wouldn't listen!")

