import tkinter as tk
from tkinter import messagebox
import pyperclip

# ---------------- CAESAR FUNCTION ----------------
def caesar_cipher(text, shift, mode):

    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:

        if char.isalpha():

            start = ord('A') if char.isupper() else ord('a')

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        else:
            result += char

    return result


# ---------------- ENCRYPT ----------------
def encrypt_text():

    text = entry.get()
    shift = shift_entry.get()

    if not text or not shift:
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        shift = int(shift) % 26
    except:
        messagebox.showerror("Error", "Shift must be a number")
        return

    result = caesar_cipher(text, shift, "encrypt")
    output_label.config(text="Encrypted: " + result)

    save_history(text, result, shift, "Encrypt")


# ---------------- DECRYPT ----------------
def decrypt_text():

    text = entry.get()
    shift = shift_entry.get()

    if not text or not shift:
        messagebox.showerror("Error", "Fill all fields")
        return

    try:
        shift = int(shift) % 26
    except:
        messagebox.showerror("Error", "Shift must be a number")
        return

    result = caesar_cipher(text, shift, "decrypt")
    output_label.config(text="Decrypted: " + result)

    save_history(text, result, shift, "Decrypt")


# ---------------- COPY ----------------
def copy_result():
    pyperclip.copy(output_label.cget("text"))
    messagebox.showinfo("Copied", "Result copied!")


# ---------------- SAVE HISTORY ----------------
def save_history(text, result, shift, mode):
    with open("caesar_history.txt", "a") as f:
        f.write(f"{mode} | {text} | {shift} -> {result}\n")


# ---------------- CLEAR ----------------
def clear_all():
    entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    output_label.config(text="")


# ---------------- UI ----------------
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("400x350")
root.config(bg="#1e1e1e")

tk.Label(root, text="Caesar Cipher Tool", font=("Arial", 16), fg="white", bg="#1e1e1e").pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)
shift_entry.insert(0, "Shift Value")

tk.Button(root, text="Encrypt", command=encrypt_text, bg="green", fg="white").pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt_text, bg="blue", fg="white").pack(pady=5)

output_label = tk.Label(root, text="", fg="yellow", bg="#1e1e1e")
output_label.pack(pady=10)

tk.Button(root, text="Copy Result", command=copy_result, bg="orange").pack(pady=5)
tk.Button(root, text="Clear", command=clear_all, bg="red", fg="white").pack(pady=5)

root.mainloop()