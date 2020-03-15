import sys
import binascii
import json
import base64

from utils.aes_util import AESUtil
from utils.rsa_util import RSAUtil

def main(target_file_name, path_to_rsa_pub_key, result_file_name, prv_key, pass_phrase):

    p_version = "0.1.0"
    aes_util = AESUtil()
    with open(target_file_name, 'rb') as f:
        target = f.read()
        enc_content = aes_util.encrypt(target)
    
    content_key = aes_util.get_aes_key()
    
    with open(path_to_rsa_pub_key, 'r') as f2:
        pkey_data = f2.read()

    with open( prv_key, 'r') as f3:
        s = f3.read()
        my_prvkey = binascii.unhexlify(s)

    rsa_util = RSAUtil()
    rsa_util.import_prv_key(my_prvkey, pass_phrase)
    enc_key = rsa_util.encrypt_with_pubkey(content_key, pkey_data)
    
    result = {}
    result["version"] = p_version
    result["file_name"] = target_file_name
    content_key_txt = binascii.hexlify(base64.b64encode(enc_key)).decode('ascii')
    result["content_key"] = content_key_txt
    content_txt = binascii.hexlify(base64.b64encode(enc_content)).decode('ascii') 
    result["content"] = content_txt
    sender_pub_key = binascii.hexlify(rsa_util.get_my_pubkey()).decode('ascii')
    result["sender"] = sender_pub_key
    
    signature = rsa_util.compute_digital_signature(p_version + target_file_name + content_key_txt + content_txt + sender_pub_key)
    result["signature"] = signature
    
    with open(result_file_name, 'w') as f4:
        json.dump(result, f4, indent=4)


if __name__ == '__main__':
    args = sys.argv
 
    if len(args) == 6:
        target = args[1]
        pub_key = args[2]
        result = args[3]
        prv_key = args[4]
        pass_phrase = args[5]
    else:
        print('Param Error')
        print('$ enc_and_sign.py <target_file_name> <path_to_rsa_pub_key> <result_file_name> <path_to_rsa_prv_key> <pass_phrase>')
        quit()

    main(target, pub_key, result, prv_key, pass_phrase)