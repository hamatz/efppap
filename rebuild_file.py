import sys
import json

import hashlib

def rebuild_file(info_list, target_file_name):

    with open(target_file_name, 'wb') as save_file:
        for f in info_list:
            data = open(f, "rb").read()
            save_file.write(data)
            save_file.flush()

def main(rebuild_info_file_name):
  with open(rebuild_info_file_name, "rb") as f:
     json_data = json.load(f)
     info_list = json_data['info_list']
     md = json_data['md']
     original_f_name = json_data['original_file_name']

  rebuild_file(info_list, original_f_name)

  sha256_hash = hashlib.sha256()
  with open(original_f_name,"rb") as f2:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f2.read(4096),b""):
        sha256_hash.update(byte_block)
    file_hash = sha256_hash.hexdigest()

    if(file_hash == md):
      print('file was verified.')
    else:
      print('oops! It seems, there is something wrong with this package')

if __name__ == "__main__":
    args = sys.argv
 
    if len(args) == 2:
        rebuild_info_file_name = args[1]

    else:
        print('Param Error')
        print('$ rebuild_file.py rebuild_info_file_name')
        quit()

    main(rebuild_info_file_name)