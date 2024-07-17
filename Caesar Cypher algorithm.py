import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = chr((ord(char) + shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted_char = chr((ord(char) - shift_amount - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift_amount - 97) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def encrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher_encrypt(message, shift)
    result_label.config(text=f"Encrypted message: {encrypted_message}")

def decrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher_decrypt(message, shift)
    result_label.config(text=f"Decrypted message: {decrypted_message}")

def main():
    global message_entry, shift_entry, result_label

    root = tk.Tk()
    root.title("Caesar Cipher")

    tk.Label(root, text="Message:").grid(row=0, column=0, padx=10, pady=10)
    message_entry = tk.Entry(root, width=50)
    message_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Shift:").grid(row=1, column=0, padx=10, pady=10)
    shift_entry = tk.Entry(root, width=5)
    shift_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
    encrypt_button.grid(row=2, column=0, padx=10, pady=10)

    decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
    decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    result_label = tk.Label(root, text="Result will be shown here", wraplength=400)
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
