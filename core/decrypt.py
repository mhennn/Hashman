from dotenv import load_dotenv
from core.get_message_key import GetKey
from cryptography.fernet import Fernet
import os
load_dotenv()

class Decrypt:
    def __init__(self):
        self.key = ""
        self.get_key = GetKey()

    def decrypt_message(self, token, password):
        try:
            salt = os.getenv("SALT")
            salt_bytes = salt.encode()
            self.key = self.get_key.get_key(password, salt_bytes)
            return Fernet(self.key).decrypt(token.encode()).decode()
        except Exception:
            return None