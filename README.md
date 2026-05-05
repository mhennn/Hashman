# Hashman 🔐🥷

---

##### Want to keep your message hidden in public? Hashman is your on the go secret messaging app

### How it works?
- Creation Mode
---> Input Message
---> Input Password
---> Generate Link

- Viewing Mode
---> Paste the Generated Link
---> Enter Password
---> Unlock

### Encryption Method
Hashman uses cryptography as its primary method of encrypting message, it includes random salt, SHA256 (Secure Hash Algorithm 256-bit) that turns any text into a unique 256-bit string.

```bash
def get_key(self, password: str, salt: bytes):
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        return base64.urlsafe_b64encode(self.kdf.derive(password.encode()))
```

### Streamlit Interface
##### Creation Mode
![creation_mode](/sample_img/creation_mode.png)

##### Viewing Mode
![viewing_mode](/sample_img/viewing_mode.png)

### Installation Method
1. Environment (Create variable "SALT" here)
```bash
py -m venv .venv
```
```bash
.venv\Scripts\activate
```
2. Requirements Installation
```bash
pip install -r requirements.txt
```
3. Application Usage
```bash
streamlit run app.py
```