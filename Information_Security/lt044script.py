import hashlib
import sys

inValue = (sys.argv[1])
hash_object = hashlib.pbkdf2_hmac('sha512', inValue.encode(), b'Km5d5ivMy8iexuHcZrsD', 200000)
hex_dig = hash_object.hex()
print(hex_dig)



