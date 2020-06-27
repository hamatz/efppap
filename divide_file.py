import sys
import json

import hashlib

def divide_file(target_file_name, chunk_size):

    with open(target_file_name, "rb") as f:
      while True:
        chunk = f.read(chunk_size)
        if chunk:
            yield chunk
        else:
            break

def main(target_file_name, chunk_size):

  i = 0
  file_list = []

  for b in divide_file(target_file_name, chunk_size):
    save_file_path = target_file_name + "." + str(i)
    with open(save_file_path, 'wb') as save_file:
        save_file.write(b)

    i = i + 1
    file_list.append(save_file_path)

  sha256_hash = hashlib.sha256()
  with open(target_file_name,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    file_hash = sha256_hash.hexdigest()

    rebuild_info = {
      'md' : file_hash,
      'info_list' : file_list, 
      'original_file_name' : target_file_name
    }

    rebuild_info_json = json.dumps(rebuild_info)

  with open("rebuild_info.json", 'w') as info_file:
    info_file.write(rebuild_info_json)


if __name__ == "__main__":
    args = sys.argv
 
    if len(args) == 3:
        target_file_name = args[1]
        chunk_size = args[2]

    else:
        print('Param Error')
        print('$ divide_file.py target_file_name, chunk_size')
        quit()

    main(target_file_name, int(chunk_size))