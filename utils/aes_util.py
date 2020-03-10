from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

import random
import string

class AESUtil:

    def __init__(self):
        sha = SHA256.new()
        k_seed = ''.join(random.choices(string.ascii_letters + string.digits, k=AES.block_size))
        sha.update(k_seed.encode())
        self.secret_key = sha.digest()

    def get_aes_key(self):
        return self.secret_key

    def encrypt(self, data):
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.secret_key, AES.MODE_CFB, iv)
        return iv + cipher.encrypt(data)

    def decrypt_with_key(self, data, key):
        iv, cdata = data[:AES.block_size], data[AES.block_size:]
        cipher = AES.new(key, AES.MODE_CFB, iv)
        return cipher.decrypt(cdata)