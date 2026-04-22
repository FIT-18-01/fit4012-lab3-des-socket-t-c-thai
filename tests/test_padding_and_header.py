from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def pad(data: bytes) -> bytes:
    pad_len = 8 - len(data) % 8
    return data + bytes([pad_len] * pad_len)


def unpad(data: bytes) -> bytes:
    pad_len = data[-1]
    return data[:-pad_len]
def encrypt_des_cbc(data: bytes):
    key = get_random_bytes(8)   
    iv = get_random_bytes(8)  

    cipher = DES.new(key, DES.MODE_CBC, iv)
    cipher_bytes = cipher.encrypt(pad(data))

    return key, iv, cipher_bytes

def build_packet(key: bytes, iv: bytes, cipher_bytes: bytes) -> bytes:
    length = len(cipher_bytes).to_bytes(4, 'big')
    return key + iv + length + cipher_bytes


def parse_header(header: bytes):
    key = header[:8]
    iv = header[8:16]
    length = int.from_bytes(header[16:20], 'big')
    return key, iv, length