import Crypto

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import binascii

class RSAUtil:

    def __init__(self):
        pass

    def encrypt_with_pubkey(self, target, pubkey_text):
        """
        与えられた公開鍵で暗号化する
        """
        pubkey = RSA.importKey(binascii.unhexlify(pubkey_text))
        
        encryptor = PKCS1_OAEP.new(pubkey)
        encrypted = encryptor.encrypt(target)
        return encrypted

    def decrypt_with_private_key(self, target):
        """
        秘密鍵で復号する
        """
        decrypter = PKCS1_OAEP.new(self._private_key)
        decrypto = decrypter.decrypt(target)
        return decrypto

    def import_prv_key(self, key_data, pass_phrase):
        """
        PEMフォーマットでパスワード保護された秘密鍵をファイルから読み込んで設定する
        """
        self._private_key = RSA.importKey(key_data, pass_phrase)
        self._public_key = self._private_key.publickey()
