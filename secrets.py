import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Path to store secret key
SECRET_KEY_PATH = os.path.expanduser("~/.secrets/secret.key")

def generate_and_save_key():
    """
    Generates a new Fernet key and saves it to SECRET_KEY_PATH.
    Run this once during setup.
    """
    os.makedirs(os.path.dirname(SECRET_KEY_PATH), exist_ok=True)
    key = Fernet.generate_key()
    with open(SECRET_KEY_PATH, "wb") as key_file:
        key_file.write(key)
    os.chmod(SECRET_KEY_PATH, 0o600)
    print(f"Key generated and saved to {SECRET_KEY_PATH}")

def load_key():
    """
    Loads the secret key from SECRET_KEY_PATH.
    """
    if not os.path.exists(SECRET_KEY_PATH):
        raise FileNotFoundError(f"Secret key not found at {SECRET_KEY_PATH}. Run generate_and_save_key() first.")
    with open(SECRET_KEY_PATH, "rb") as key_file:
        return key_file.read()

def encrypt_password(plain_text_password: str) -> str:
    """
    Encrypts the given plain-text password.
    """
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(plain_text_password.encode())
    return encrypted.decode()

def decrypt_password(encrypted_password: str) -> str:
    """
    Decrypts the given encrypted password.
    """
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()

def get_decrypted_password_from_env(env_key: str = "ENCRYPTED_DB_PASSWORD") -> str:
    """
    Loads and decrypts the encrypted DB password from the environment or .env file.
    """
    load_dotenv()
    encrypted = os.getenv(env_key)
    if not encrypted:
        raise ValueError(f"Environment variable '{env_key}' not set.")
    return decrypt_password(encrypted)
