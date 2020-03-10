from utils.aes_util import AESUtil
from utils.rsa_util import RSAUtil

import sys
import binascii
import json
import base64

def main(target_file_name, path_to_rsa_pub_key, result_file_name):
    aes_util = AESUtil()
    target_data = open(target_file_name, "rb")
    target = target_data.read()
    enc_content = aes_util.encrypt(target)
    target_data.close()
    
    content_key = aes_util.get_aes_key()
    
    p_file = open(path_to_rsa_pub_key, "r")
    pkey_data = p_file.read()

    rsa_util = RSAUtil()
    enc_key = rsa_util.encrypt_with_pubkey(content_key, pkey_data)
    
    result = {}
    result["version"] = "0.1.0"
    result["file_name"] = target_file_name
    result["content_key"] = binascii.hexlify(base64.b64encode(enc_key)).decode('ascii')
    result["content"] = binascii.hexlify(base64.b64encode(enc_content)).decode('ascii') 
    
    with open(result_file_name, 'w') as f:
        json.dump(result, f, indent=4)


if __name__ == '__main__':
    args = sys.argv
 
    if len(args) == 4:
        target = args[1]
        pub_key = args[2]
        result = args[3]
    else:
        print('Param Error')
        print('$ enc.py <target_file_name> <path_to_rsa_pub_key> <result_file_name>')
        quit()

    main(target, pub_key, result)