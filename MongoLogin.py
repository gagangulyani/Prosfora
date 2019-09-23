from models.encryption import Encrypt, Decrypt
from models.user import User

def encSession(s):
    return Encrypt(s)

def decSession(s,k):
    return Decrypt(s,k)
