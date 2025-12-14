# 🔐 Custom Substitution Cipher Generator

A Python-based cryptography project that implements a **Custom Substitution Cipher** with both **encryption and decryption** support.  
The project includes a **GUI application**, key generation, and test scripts to verify correctness.

---

## 📌 Project Overview

A substitution cipher replaces each character in the plaintext with another character based on a **secret substitution key**.  
This project demonstrates:
- How encryption and decryption work
- Key generation and usage
- Basic cryptographic concepts
- GUI-based interaction for ease of use

This project is suitable for:
- Cryptography mini-projects
- Academic evaluation
- Beginners learning encryption concepts

---

## ✨ Features

- Random substitution key generation
- Encryption of plaintext messages
- Decryption using the same key
- GUI-based interface (Tkinter)
- Test scripts for validation
- Simple and readable Python implementation

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** (for GUI)
- File handling for key management

---

## 📂 Project Structure

```text
Custom-CipherProject/
│
├── cipher_tool.py        # Core encryption & decryption logic
├── gui_app.py            # GUI application
├── test_cipher.py        # Test cases for cipher logic
├── verify_results.py     # Verification script
├── status.txt            # Status/output file
├── README.md             # Project documentation
└── .gitignore            # Ignored files configuration

⚙️ Installation & Setup
1️⃣ Prerequisites

Ensure you have Python 3.8 or above installed.

Check Python version:

python --version

2️⃣ Clone the Repository
git clone https://github.com/deepith-18/Custom-Substitution-Cipher-Generator.git
cd Custom-Substitution-Cipher-Generator
▶️ How to Run the Project
🔹 Run the GUI Application
python gui_app.py


This will open a graphical interface where you can:

Enter plaintext

Encrypt the message

Decrypt using the same key
Run Encryption/Decryption via Script
python cipher_tool.py

🔹 Run Test Scripts
python test_cipher.py
python verify_results.py


These scripts verify that encryption and decryption work correctly.

🔑 Key Management

A random substitution key is generated automatically

The same key is required for decryption

The key file is ignored from Git for security reasons
📖 Example

Plaintext:

HELLO WORLD


Encrypted Text:

QZMMF DFPMW


Decrypted Text:

HELLO WORLD
