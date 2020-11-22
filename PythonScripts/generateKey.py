'''
Generate a key with random 96 chars.
'''
import random
import string
import qrCodeGenerator

def get_random_string():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(10))
    print(password)
    return password

if __name__ == "__main__":
    password = get_random_string()
    qrCodeGenerator.create_qr_code('example', 'WPA2', password)