import hashlib
import sys
import random
import string

def random_string(l = 20):
    return ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(l))

salt = random_string()

inValue = (sys.argv[1])

hash_object = hashlib.pbkdf2_hmac('sha512', inValue.encode(), salt.encode(), 200000)
hex_dig = hash_object.hex()
print(hex_dig)



