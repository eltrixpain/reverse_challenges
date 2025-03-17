import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64
import random

FLAG = "JlLScp2qTzfFZ7kIYP6Jm5Mv/2h6p26S0OWgmXYdEMAl1Sjg6hwW95bPsZdtiggvHVVv8zM+x7vRw2qOr3ORbw=="

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
            decryptedBytes = unpad(cipher.decrypt(encryptedData[16:]), AES.block_size).decode()
        except:
            return ""
        return decryptedBytes
    
def find_paths(graph, start, end, path=None, max_depth=23):
    if path is None:
        path = [start]
    
    if len(path) >= max_depth:
        return []
    
    if start == end and len(path) < max_depth:
        return [path]
    
    paths = []
    for node in graph.get(start, []):
        new_paths = find_paths(graph, node, end, path + [node], max_depth)
        paths.extend(new_paths)
    
    return paths

def checkFlag(path):
    aes = Cipher()

    a = "" 
    b = ""
    for p in path:
        if path.index(p) % 2 == 0:
            a += f"{p[0]+p[-1]}"
        else:
            b += f"{p[0]+p[-1]}"

    key = a+b
    attempt = aes.decrypt(FLAG,key)
    if "KSUS" not in attempt:
        pass
    else:
        print(attempt)
        print(path)
        exit()

# Print all valid paths
# for path in paths:
#     print(" -> ".join(path))

routes = {
   "Cemetery of Ash": ["Firelink Shrine"],
   "Grand Archives": ["Lothric Castle", "High Wall of Lothric"],
   "Profaned Capital": ["Irithyll Dungeon"],
   "Farron Keep": ["Road of Sacrifices", "Catacombs of Carthus"],
   "Anor Londo": ["Irithyll of the Boreal Valley"],
   "High Wall of Lothric": ["Firelink Shrine", "Undead Settlement", "Lothric Castle", "Untended Graves"],
   "Undead Settlement": ["High Wall of Lothric", "Road of Sacrifices"],
   "Firelink Shrine": ["Kiln of the First Flame", "High Wall of Lothric"],
   "Road of Sacrifices": ["Cathedral of the Deep", "Farron Keep", "Undead Settlement"],
   "Irithyll Dungeon": ["Irithyll of the Boreal Valley"],
   "Catacombs of Carthus": ["Farron Keep", "Irithyll of the Boreal Valley"],
   "Lothric Castle": ["High Wall of Lothric", "Untended Graves", "Grand Archives"],
   "Cathedral of the Deep": ["Farron Keep", "Road of Sacrifices"],
   "Irithyll of the Boreal Valley": ["Anor Londo", "Irithyll Dungeon", "Catacombs of Carthus"],
   "Untended Graves": ["Lothric Castle"]
}



start_node = "Cemetery of Ash"
end_node = "Kiln of the First Flame"
paths = find_paths(routes, start_node, end_node)
print(len(paths))
# for i in paths:
#     print(i)
for path in paths:
    checkFlag(path)
