'''
Generate a key with random 96 chars.
'''
import random
import string
import qrCodeGenerator

def get_random_string():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(10))
    return password

if __name__ == "__main__":
    print(get_random_string())