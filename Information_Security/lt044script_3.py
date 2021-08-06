import hashlib
import sys
import random
import string

def random_string(l = 20):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(l))

salt = random_string()

inValue = (sys.argv[1])

hash_object = hashlib.sha512(salt.encode() + inValue.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)


