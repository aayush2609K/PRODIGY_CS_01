import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt_decrypt():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    mode = mode_var.get()

    if mode not in ['encrypt', 'decrypt']:
        messagebox.showerror("Error", "Invalid mode! Please enter 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(text, shift, mode)
    output_text.delete("1.0", "end")
    output_text.insert("end", result)

root = tk.Tk()
root.title("Caesar Cipher")
root.configure(background="#ffffff")

main_frame = ttk.Frame(root, padding="20", style="My.TFrame")
main_frame.grid(row=10, column=10, sticky="nsew")

style = ttk.Style()
style.configure("My.TFrame", background="#6497b1")
style.configure("My.TLabel", background="#6497b1", font=("Times Roman", 12, "bold"))
style.configure("My.TButton", background="#011f4b", foreground="#ffffff", font=("Times Roman", 12, "bold"))

ttk.Label(main_frame, text="Enter the text:", style="My.TLabel").grid(row=0, column=0, sticky="w")
input_text = tk.Text(main_frame, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=3, padx=(0, 10), pady=5, sticky="w")

ttk.Label(main_frame, text="Enter the shift value:", style="My.TLabel").grid(row=2, column=0, sticky="w")
shift_entry = ttk.Entry(main_frame, width=13)
shift_entry.grid(row=2, column=1, pady=5, sticky="w")

ttk.Label(main_frame, text="Select 'encrypt' or 'decrypt':", style="My.TLabel").grid(row=3, column=0, sticky="w")
mode_var = tk.StringVar(value="encrypt")
mode_combobox = ttk.Combobox(main_frame, textvariable=mode_var, values=["encrypt", "decrypt"], width=10)
mode_combobox.grid(row=3, column=1, pady=5, sticky="w")

encrypt_button = tk.Button(main_frame, text="Encrypt / Decrypt", command=encrypt_decrypt, bg="#011f4b", fg="white", font=("Times Roman", 12, "bold"))
encrypt_button.grid(row=4, column=0, columnspan=2, pady=10)


ttk.Label(main_frame, text="Result:", style="My.TLabel").grid(row=5, column=0, sticky="w")
output_text = tk.Text(main_frame, height=5, width=40)
output_text.grid(row=6, column=0, columnspan=3, padx=(0, 10), pady=5, sticky="w")

root.mainloop()