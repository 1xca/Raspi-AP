'''
Generate a key with random 94 chars.
'''
import random
import string
import qrCodeGenerator

def get_random_password():
    temp = string.ascii_letters + string.digits + string.punctuation
    
    #remove problematic characters
    alphabet = temp.replace('\'', '').replace('\\', '').replace('\"', '').replace('\`', '').replace(';', '')

    #generate a random password
    password = ''.join(random.choice(alphabet) for i in range(10))
    return password

if __name__ == "__main__":
    print(get_random_password())