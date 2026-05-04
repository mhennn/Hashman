import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from dotenv import load_dotenv
import os
load_dotenv()

class GetKey:
    def __init__(self):
        self.kdf = ""

    def get_key(self, password: str, bytes: bytes):
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=os.getenv("SALT"),
            iterations=100000
        )
        return base64.urlsafe_b64encode(self.kdf.derive(password.encode()))