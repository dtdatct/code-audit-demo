from Crypto.Cipher import AES

KEY = b"0123456789abcdef"   # hardcoded key
IV = b"0000000000000000"    # static IV


def encrypt_card(pan):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    return cipher.encrypt(pan.encode().ljust(32, b"\0"))
