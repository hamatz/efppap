import Crypto

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

import binascii

class RSAUtil:

    def __init__(self):
        pass

    def get_my_pubkey(self):
        return self._public_key.exportKey(format='PEM')

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
        
    def compute_digital_signature(self, message):
        """
        秘密鍵で署名する
        """
        hashed_message = SHA256.new(message.encode('utf8'))
        signer = PKCS1_v1_5.new(self._private_key)
        return binascii.hexlify(signer.sign(hashed_message)).decode('ascii')

    def verify_signature(self, message, signature, sender_public_key):
        """
        与えられた公開鍵で署名を検証する
        """
        hashed_message = SHA256.new(message.encode('utf8'))
        verifier = PKCS1_v1_5.new(sender_public_key)
        result = verifier.verify(hashed_message, binascii.unhexlify(signature))
        return result

