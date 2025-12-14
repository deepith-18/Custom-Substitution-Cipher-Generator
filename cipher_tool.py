import random
import string
import os

# CONSTANTS
ALPHABET = string.ascii_letters # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY_FILE = "key.txt"

def generate_key():
    """
    Generates a random substitution key.
    The key is a shuffled version of the ALPHABET.
    """
    key_list = list(ALPHABET)
    random.shuffle(key_list)
    key = "".join(key_list)
    return key

def save_key(key):
    """
    Saves the generated key to a file.
    """
    try:
        with open(KEY_FILE, "w") as f:
            f.write(key)
        print(f"\n[SUCCESS] Key saved to '{KEY_FILE}'.")
    except IOError as e:
        print(f"\n[ERROR] Could not save key: {e}")

def load_key():
    """
    Loads the key from the file.
    Returns the key as a string, or None if file not found.
    """
    if not os.path.exists(KEY_FILE):
        print(f"\n[ERROR] Key file '{KEY_FILE}' not found! Please generate a new key first.")
        return None
    
    try:
        with open(KEY_FILE, "r") as f:
            key = f.read().strip()
        
        # Simple validation
        if len(key) != len(ALPHABET):
            print("\n[ERROR] Key file is corrupted (wrong length). Please generate a new key.")
            return None
            
        return key
    except IOError as e:
        print(f"\n[ERROR] Could not read key file: {e}")
        return None

def encrypt(message, key):
    """
    Encrypts a message using the substitution key.
    Each character in ALPHABET is replaced by the corresponding character in key.
    """
    encrypted_message = ""
    for char in message:
        if char in ALPHABET:
            # Find the index of the character in the normal alphabet
            index = ALPHABET.index(char)
            # Replace it with the character at the same index in the key
            encrypted_message += key[index]
        else:
            # Keep special characters, numbers, and spaces as is
            encrypted_message += char
    return encrypted_message

def decrypt(ciphertext, key):
    """
    Decrypts a message using the substitution key.
    Reverses the process: finds char in key, maps back to ALPHABET.
    """
    decrypted_message = ""
    for char in ciphertext:
        if char in ALPHABET: # Note: The key contains the same characters as ALPHABET, just shuffled
             # Find the index of the character in the *key*
            index = key.index(char)
            # Replace it with the character at the same index in the original alphabet
            decrypted_message += ALPHABET[index]
        else:
            decrypted_message += char
    return decrypted_message

def main():
    """
    Main program loop showing the menu.
    """
    print("--- Custom Substitution Cipher Generator ---")
    
    while True:
        print("\nOPTIONS:")
        print("1. Generate New Key")
        print("2. Encrypt Message")
        print("3. Decrypt Message")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            print("\nGenerating new key...")
            key = generate_key()
            save_key(key)
            # educational output
            print(f"Debug Info: Alphabet Length: {len(ALPHABET)}, Key Length: {len(key)}")
            
        elif choice == '2':
            key = load_key()
            if key:
                message = input("\nEnter message to encrypt: ")
                ciphertext = encrypt(message, key)
                print(f"\nencrypted message: {ciphertext}")
                
        elif choice == '3':
            key = load_key()
            if key:
                ciphertext = input("\nEnter message to decrypt: ")
                plaintext = decrypt(ciphertext, key)
                print(f"\nDecrypted Message: {plaintext}")
                
        elif choice == '4':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\n[INVALID] Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
