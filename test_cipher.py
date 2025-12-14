import unittest
import os
import string
from cipher_tool import generate_key, save_key, load_key, encrypt, decrypt, ALPHABET, KEY_FILE

class TestCipherTool(unittest.TestCase):
    
    def setUp(self):
        # Ensure we start with a clean state for key file
        if os.path.exists(KEY_FILE):
            os.remove(KEY_FILE)

    def tearDown(self):
        # Clean up after tests
        if os.path.exists(KEY_FILE):
            os.remove(KEY_FILE)

    def test_key_generation(self):
        key = generate_key()
        self.assertEqual(len(key), len(ALPHABET), "Key length must match alphabet length")
        self.assertEqual(sorted(key), sorted(ALPHABET), "Key must be a permutation of alphabet")
        self.assertNotEqual(key, ALPHABET, "Key should not match alphabet exactly (highly unlikely)")

    def test_save_load_key(self):
        key = generate_key()
        save_key(key)
        loaded_key = load_key()
        self.assertEqual(key, loaded_key, "Loaded key must match saved key")

    def test_encryption_decryption(self):
        key = generate_key()
        message = "Hello World! 123"
        ciphertext = encrypt(message, key)
        decrypted = decrypt(ciphertext, key)
        self.assertEqual(decrypted, message, "Decrypted message must match original")
        self.assertNotEqual(ciphertext, message, "Ciphertext should differ from message")

    def test_special_characters(self):
        key = generate_key()
        message = "!@#$%^&*()_+ 1234567890"
        encrypted = encrypt(message, key)
        self.assertEqual(encrypted, message, "Special characters and numbers should be preserved")

    def test_missing_key_file(self):
        # key file is ensured to not exist by setUp
        loaded_key = load_key()
        self.assertIsNone(loaded_key, "Loading missing key should return None")

if __name__ == '__main__':
    unittest.main()
