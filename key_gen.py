import Crypto
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256

import binascii
import sys

def main(my_pass):
    random_gen = Crypto.Random.new().read
    _private_key = RSA.generate(2048, random_gen)
    _public_key = _private_key.publickey()
    _signer = PKCS1_v1_5.new(_private_key)
    my_pem = _private_key.exportKey(format='PEM', passphrase=my_pass)
    my_pem_hex = binascii.hexlify(my_pem).decode('ascii')

    # とりあえずファイル名は固定
    path = 'my_private_key.pem'
    f1 = open(path,'a')
    f1.write(my_pem_hex)
    f1.close()

    path2 = 'my_public_key.pem'
    my_pub_pem = _public_key.exportKey(format='PEM')
    my_pub_pem_hex = binascii.hexlify(my_pub_pem).decode('ascii')
    f2 = open(path2,'a')
    f2.write(my_pub_pem_hex)
    f2.close()

if __name__ == '__main__':
    args = sys.argv
 
    if len(args) == 2:
        my_pass = args[1]

    else:
        print('Param Error')
        print('$ enc.py <my_pass>')
        quit()

    main(my_pass)