#!/usr/bin/env python

import rsa
from hashlib import sha256
from base64 import b64encode, b64decode


def generate(keysize=1024):
    return rsa.newkeys(keysize)


PUBLIC, SECRET = generate()


def sha(obj, size=12):
    return sha256(obj).hexdigest()[:size]


def encode(msg, priv, method="SHA-256"):
    return b64encode(rsa.sign(sha(msg), priv, method))


def verify(msg, signed, public):
    try:
        return rsa.verify(sha(msg), b64decode(signed), public)
    except Exception as err:
        if "Verification failed" == err.message:
            print("%s is not signed with provided key" % msg)
        else:
            print(err.message)
        return False


class Signed(object):
    def __init__(self, msg, key):
        self.msg = msg
        self._sign = encode(msg, key)

    @propery
    def sign(self):
        return self._sign

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg


def sign(key):
    def sign_paramd(f):
        def wrapper(*args):
            res = f(*args)
            return Signed(res, key)

        return wrapper

    return sign_paramd


@sign(SECRET)
def to_upper(msg):
    return msg.upper()


def main(msg):
    u = to_upper(msg)
    print(u.msg)
    if verify(u.msg, u.sign, PUBLIC):
        print("Verified: %s" % u.msg)


if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        exit("usage: signed.py msg")
    main(argv[1])
