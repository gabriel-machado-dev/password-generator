import random
import string
import customtkinter as ctk

# Define character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self.root, text="Password Generator", font=("Arial", 20))
        title_label.pack(pady=10, anchor='center')

        length_label = ctk.CTkLabel(self.root, text="Enter the desired password length:")
        length_label.pack(pady=5, anchor='center')
        self.length_entry = ctk.CTkEntry(self.root)
        self.length_entry.pack(pady=5, anchor='center')

        self.uppercase_var = ctk.BooleanVar()
        self.lowercase_var = ctk.BooleanVar()
        self.digits_var = ctk.BooleanVar()
        self.symbols_var = ctk.BooleanVar()

        uppercase_check = ctk.CTkCheckBox(self.root, text="Include uppercase letters", variable=self.uppercase_var)
        uppercase_check.pack(pady=5, anchor='center')
        lowercase_check = ctk.CTkCheckBox(self.root, text="Include lowercase letters", variable=self.lowercase_var)
        lowercase_check.pack(pady=5, anchor='center')
        digits_check = ctk.CTkCheckBox(self.root, text="Include digits", variable=self.digits_var)
        digits_check.pack(pady=5, anchor='center')
        symbols_check = ctk.CTkCheckBox(self.root, text="Include symbols", variable=self.symbols_var)
        symbols_check.pack(pady=5, anchor='center')

        generate_button = ctk.CTkButton(self.root, text="Generate Password", command=self.generate_password)
        generate_button.pack(pady=20, anchor='center')

        self.result_label = ctk.CTkLabel(self.root, text="")
        self.result_label.pack(pady=10, anchor='center')

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            self.result_label.configure(text="Please enter a valid number for length.")
            return

        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_digits = self.digits_var.get()
        include_symbols = self.symbols_var.get()

        all_characters = self.get_all_characters(include_uppercase, include_lowercase, include_digits, include_symbols)

        if len(all_characters) == 0:
            self.result_label.configure(text="No characters selected, password cannot be generated.")
            return

        if length > len(all_characters):
            self.result_label.configure(text="Password length exceeds available characters.")
            return

        password = ''.join(random.sample(all_characters, length))
        self.result_label.configure(text=f"Generated password: {password}")

    def get_all_characters(self, include_uppercase, include_lowercase, include_digits, include_symbols):
        all_characters = ''
        if include_uppercase:
            all_characters += uppercase
        if include_lowercase:
            all_characters += lowercase
        if include_digits:
            all_characters += digits
        if include_symbols:
            all_characters += symbols
        return all_characters

if __name__ == "__main__":
    app = ctk.CTk()
    PasswordGeneratorApp(app)
    app.mainloop()
