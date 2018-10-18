"""Mosquitto PBKDF2 password libray.

from https://github.com/jpmens/mosquitto-auth-plug
"""
import hashlib
from os import urandom
import hmac
from struct import Struct
from operator import xor
from itertools import starmap
from base64 import b64encode

SALT_LENGTH = 12
KEY_LENGTH = 24
HASH_FUNCTION = 'sha256'
COST_FACTOR = 10000

_pack_int = Struct('>I').pack


def pbkdf2_hex(data, salt, iterations=1000, keylen=24, hashfunc=None):
    """Like :func:`pbkdf2_bin` but returns a hex encoded string."""
    return pbkdf2_bin(data, salt, iterations, keylen, hashfunc).encode('hex')


def ord3(arg):
    return ord(chr(arg))


def chr3(arg):
    return chr(arg).encode('latin-1')


def pbkdf2_bin(data, salt, iterations=1000, keylen=24, hashfunc=None):
    """Returns a binary digest for the PBKDF2 hash algorithm of `data`
    with the given `salt`.  It iterates `iterations` time and produces a
    key of `keylen` bytes.  By default SHA-1 is used as hash function,
    a different hashlib `hashfunc` can be provided.
    """
    hashfunc = hashfunc or hashlib.sha1
    mac = hmac.new(data, None, hashfunc)

    def _pseudorandom(x, mac=mac):
        h = mac.copy()
        if type(x) is str:
            x = bytes(x, "utf-8")
        h.update(x)
        return list(map(ord3, h.digest()))
    buf = []
    for block in range(1, -(-keylen // mac.digest_size) + 1):
        rv = u = _pseudorandom(salt + _pack_int(block))
        for i in range(iterations - 1):
            u = _pseudorandom(b''.join(map(chr3, u)))
            rv = starmap(xor, zip(rv, u))
        buf.extend(rv)
    return b''.join(map(chr3, buf))[:keylen]


def make_hash(password):
    """Generate a random salt and return a new hash for the password."""
    if isinstance(password, str):
        password = password.encode('utf-8')
    salt = b64encode(urandom(SALT_LENGTH))
    return 'PBKDF2${}${}${}${}'.format(
        HASH_FUNCTION,
        COST_FACTOR,
        str(salt, 'utf-8'),
        str(b64encode(pbkdf2_bin(
            password, salt, COST_FACTOR, KEY_LENGTH,
            getattr(hashlib, HASH_FUNCTION))), 'utf-8'))
