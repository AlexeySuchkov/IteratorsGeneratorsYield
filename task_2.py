import hashlib


def generator(path):
    with open(path, 'r') as target_file:
        for f in target_file:
            line = target_file.readline()
            hash_object = hashlib.md5(line.encode())
            yield hash_object


if __name__ == '__main__':
    for hash_obj in generator('countries.txt'):
        print(hash_obj.hexdigest())
