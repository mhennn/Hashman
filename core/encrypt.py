from dotenv import load_dotenv
from core.get_message_key import GetKey
from cryptography.fernet import Fernet
import os
load_dotenv()

class Encrypt:
    def __init__(self):
        self.get_key = GetKey()
        self.key = ""

    def encrypt_message(self, message, password):
        salt = os.getenv("SALT")
        salt_bytes = salt.encode()
        self.key = self.get_key.get_key(password, salt_bytes)
        return Fernet(self.key).encrypt(message.encode()).decode()