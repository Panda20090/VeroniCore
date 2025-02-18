# encryption_manager.py
# This script manages encryption and decryption of sensitive data, ensuring data security and privacy.

from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key=None):
        self.key = key or self.generate_key()
        self.cipher = Fernet(self.key)
        print("EncryptionManager initialized.")

    def generate_key(self):
        # Generate a new key for encryption
        key = Fernet.generate_key()
        print(f"Generated encryption key: {key.decode()}")
        return key

    def encrypt_data(self, data):
        # Encrypt data
        encrypted_data = self.cipher.encrypt(data.encode())
        print(f"Encrypted data: {encrypted_data.decode()}")
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt data
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        print(f"Decrypted data: {decrypted_data}")
        return decrypted_data

    def save_key(self, key_path="encryption_key.key"):
        # Save the encryption key to a file
        with open(key_path, 'wb') as key_file:
            key_file.write(self.key)
        print(f"Encryption key saved to {key_path}")

    def load_key(self, key_path="encryption_key.key"):
        # Load the encryption key from a file
        with open(key_path, 'rb') as key_file:
            self.key = key_file.read()
        self.cipher = Fernet(self.key)
        print(f"Encryption key loaded from {key_path}")

if __name__ == "__main__":
    # Example usage of EncryptionManager
    manager = EncryptionManager()
    
    # Encrypt some data
    data = "This is a secret message."
    encrypted = manager.encrypt_data(data)
    
    # Decrypt the data
    decrypted = manager.decrypt_data(encrypted)
    
    # Save the encryption key
    manager.save_key()
    
    # Load the encryption key
    manager.load_key()
    
    # Decrypt the data again
    decrypted_again = manager.decrypt_data(encrypted)
    