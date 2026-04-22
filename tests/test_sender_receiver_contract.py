from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def pad(data: bytes) -> bytes:
    pad_len = 8 - len(data) % 8
    return data + bytes([pad_len] * pad_len)


def encrypt_des_cbc(data: bytes, key: bytes = None, iv: bytes = None):
    if key is None:
        key = get_random_bytes(8)
    if iv is None:
        iv = get_random_bytes(8)

    cipher = DES.new(key, DES.MODE_CBC, iv)
    cipher_bytes = cipher.encrypt(pad(data))

    return key, iv, cipher_bytes