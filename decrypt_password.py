import base64
import os
from Crypto.Cipher import AES

key = os.getenv('PORT_CLIENT_SECRET')[:32].encode()

encrypted_property_value = base64.b64decode(os.getenv('PASSWORD'))

iv = encrypted_property_value[:16]
ciphertext = encrypted_property_value[16:-16]
mac = encrypted_property_value[-16:]
cipher = AES.new(key, AES.MODE_GCM, iv)

# decrypt the property
decrypted_property_value = cipher.decrypt_and_verify(ciphertext, mac)
print(f"::set-output name=decrypted_value::{decrypted_property_value}")
