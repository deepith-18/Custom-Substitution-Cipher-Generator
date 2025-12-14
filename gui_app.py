import tkinter as tk
from tkinter import messagebox, scrolledtext
import cipher_tool as cipher

class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Substitution Cipher")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        # --- Header ---
        header_frame = tk.Frame(root, bg="#333", pady=10)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame, 
            text="Substitution Cipher Generator", 
            font=("Helvetica", 18, "bold"), 
            bg="#333", 
            fg="white"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            header_frame, 
            text="Educational Cryptography Mini-Project", 
            font=("Helvetica", 10), 
            bg="#333", 
            fg="#ccc"
        )
        subtitle_label.pack()

        # --- Key Management ---
        key_frame = tk.LabelFrame(root, text="Key Management", font=("Helvetica", 12, "bold"), bg="#f0f0f0", padx=10, pady=10)
        key_frame.pack(fill=tk.X, padx=20, pady=15)
        
        self.btn_generate = tk.Button(
            key_frame, 
            text="Generate New Random Key", 
            command=self.generate_new_key,
            bg="#2196F3", 
            fg="white",
            font=("Helvetica", 10, "bold"),
            padx=10, 
            pady=5
        )
        self.btn_generate.pack(pady=5)
        
        self.lbl_key_status = tk.Label(key_frame, text="Checking key...", bg="#f0f0f0", fg="#555")
        self.lbl_key_status.pack()
        
        # Initial check
        self.update_key_status()

        # --- Encryption Section ---
        enc_frame = tk.LabelFrame(root, text="Encryption", font=("Helvetica", 12, "bold"), bg="#f0f0f0", padx=10, pady=10)
        enc_frame.pack(fill=tk.X, padx=20, pady=5)
        
        tk.Label(enc_frame, text="Message to Encrypt:", bg="#f0f0f0").pack(anchor=tk.W)
        self.entry_encrypt = tk.Entry(enc_frame, font=("Courier New", 10), width=50)
        self.entry_encrypt.pack(fill=tk.X, pady=5)
        
        self.btn_encrypt = tk.Button(
            enc_frame, 
            text="Encrypt ↓", 
            command=self.do_encrypt,
            bg="#4CAF50", 
            fg="white", 
            font=("Helvetica", 10, "bold")
        )
        self.btn_encrypt.pack(pady=5)
        
        tk.Label(enc_frame, text="Ciphertext Result:", bg="#f0f0f0").pack(anchor=tk.W)
        self.txt_encrypt_out = tk.Entry(enc_frame, font=("Courier New", 10), width=50, state='readonly')
        self.txt_encrypt_out.pack(fill=tk.X, pady=5)

        # --- Decryption Section ---
        dec_frame = tk.LabelFrame(root, text="Decryption", font=("Helvetica", 12, "bold"), bg="#f0f0f0", padx=10, pady=10)
        dec_frame.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(dec_frame, text="Ciphertext to Decrypt:", bg="#f0f0f0").pack(anchor=tk.W)
        self.entry_decrypt = tk.Entry(dec_frame, font=("Courier New", 10), width=50)
        self.entry_decrypt.pack(fill=tk.X, pady=5)
        
        self.btn_decrypt = tk.Button(
            dec_frame, 
            text="Decrypt ↓", 
            command=self.do_decrypt,
            bg="#FF9800", 
            fg="white", 
            font=("Helvetica", 10, "bold")
        )
        self.btn_decrypt.pack(pady=5)
        
        tk.Label(dec_frame, text="Original Message Result:", bg="#f0f0f0").pack(anchor=tk.W)
        self.txt_decrypt_out = tk.Entry(dec_frame, font=("Courier New", 10), width=50, state='readonly')
        self.txt_decrypt_out.pack(fill=tk.X, pady=5)

    def update_key_status(self):
        key = cipher.load_key()
        if key:
            self.lbl_key_status.config(text=f"Active Key Found: {key[:10]}... (Saved in key.txt)", fg="green")
        else:
            self.lbl_key_status.config(text="No Key Found! Please generate one.", fg="red")

    def generate_new_key(self):
        confirm = messagebox.askyesno("Confirm", "Generating a new key will make previous ciphertexts undecryptable.\nAre you sure?")
        if confirm:
            key = cipher.generate_key()
            cipher.save_key(key)
            self.update_key_status()
            messagebox.showinfo("Success", "New substitution key generated and saved.")

    def do_encrypt(self):
        key = cipher.load_key()
        if not key:
            messagebox.showerror("Error", "No key found! generate a key first.")
            return
            
        message = self.entry_encrypt.get()
        if not message:
            return
            
        ciphertext = cipher.encrypt(message, key)
        
        self.txt_encrypt_out.config(state='normal')
        self.txt_encrypt_out.delete(0, tk.END)
        self.txt_encrypt_out.insert(0, ciphertext)
        self.txt_encrypt_out.config(state='readonly')

    def do_decrypt(self):
        key = cipher.load_key()
        if not key:
            messagebox.showerror("Error", "No key found! generate a key first.")
            return
            
        ciphertext = self.entry_decrypt.get()
        if not ciphertext:
            return
            
        plaintext = cipher.decrypt(ciphertext, key)
        
        self.txt_decrypt_out.config(state='normal')
        self.txt_decrypt_out.delete(0, tk.END)
        self.txt_decrypt_out.insert(0, plaintext)
        self.txt_decrypt_out.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
