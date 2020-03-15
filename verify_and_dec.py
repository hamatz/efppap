import sys
import binascii
import json
import base64

from Crypto.PublicKey import RSA

from utils.aes_util import AESUtil
from utils.rsa_util import RSAUtil

def main(target, prv_key, pass_phrase):
    aes_util = AESUtil()
    rsa_util = RSAUtil()

    with open(prv_key) as f:
        s = f.read()
        pkey = binascii.unhexlify(s)
        rsa_util.import_prv_key(pkey, pass_phrase)

    with open(target) as f2:
        s = f2.read()
        target_data = json.loads(s)
        p_version = target_data["version"]
        file_name = target_data["file_name"]
        c_key = target_data["content_key"]
        e_content = target_data["content"]
        sender_pub_key = target_data["sender"]
        encrypted_key = base64.b64decode(binascii.unhexlify(c_key))
        decrypted_key = rsa_util.decrypt_with_private_key(encrypted_key)
        enc_data = base64.b64decode(binascii.unhexlify(e_content))
        content = aes_util.decrypt_with_key(enc_data, decrypted_key)
        signature = target_data["signature"]
        
        target_strings = p_version + file_name + c_key + e_content + sender_pub_key
        sender_pubkey = RSA.importKey(binascii.unhexlify(sender_pub_key))
        
        v_result = rsa_util.verify_signature(target_strings, signature, sender_pubkey)
        
    if(v_result):
        with open(file_name, mode='wb') as f3:
            f3.write(content)

if __name__ == '__main__':
    args = sys.argv
 
    if len(args) == 4:
        target = args[1]
        prv_key = args[2]
        pass_phrase = args[3]
    else:
        print('Param Error')
        print('$ verify_and_dec.py <path_to_target_data> <path_to_rsa_private_key> <pass_phrase>')
        quit()

    main(target, prv_key, pass_phrase)