import os

# Lets create a module to encrypt and decrypt a file.
def encrypt(file):
    encoded_file = os.fsencode(file)
    return encoded_file
    # encrypt some file
    # return said encrypted file

def decrypt(file):
    decoded_file = os.fsdecode(file)
    return decoded_file
    # decrypt file
    # return decrypted file.
