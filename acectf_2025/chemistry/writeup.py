#eltrix and llm:))))
#flag = "ACECTF{4ppr3n71c3_w4l73r_wh1t3}"
import base64
from binascii import unhexlify
from Crypto.Util.number import bytes_to_long, long_to_bytes

FERROUS_OXIDE_USERNAME = "AdminFeroxide"
ANIONIC_PASSWORD = "NjQzMzcyNzUzNTM3MzE2Njc5MzE2ZTM2"
ALKALINE_SECRET = "4143454354467B34707072336E373163335F3634322C28010D3461302C392E"
decoded_password_hex = base64.b64decode(ANIONIC_PASSWORD).decode()
decoded_password = unhexlify(decoded_password_hex).decode()
cation_hex = FERROUS_OXIDE_USERNAME.encode().hex()
anion_hex = decoded_password.encode().hex()
cation_value = bytes_to_long(unhexlify(cation_hex))
anion_value = bytes_to_long(unhexlify(anion_hex))
alkaline_secret_value = bytes_to_long(unhexlify(ALKALINE_SECRET))
covalent_link = cation_value ^ anion_value
metallic_alloy = covalent_link ^ alkaline_secret_value
flag_hex = hex(metallic_alloy)[2:]  
if len(flag_hex) % 2 != 0:  
    flag_hex = "0" + flag_hex

flag = unhexlify(flag_hex).decode()
print(flag)

