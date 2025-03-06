import customtkinter as ctk
from tkinter import PhotoImage


class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x400")
        self.configure(bg="#2E2E2E")
        self.setup_ui()
        self.mainloop()

    def setup_ui(self):
        # Load and display image
        self.image = PhotoImage(file="login.png").subsample(3, 3)
        image_label = ctk.CTkLabel(self, image=self.image, text="")
        image_label.pack(pady=10)

        # Email Entry
        email_label = ctk.CTkLabel(self, text="Email:", font=("Arial", 14))
        email_label.pack(pady=(10, 0))
        self.email_entry = ctk.CTkEntry(self, width=250)
        self.email_entry.pack(pady=5)

        # Password Entry
        password_label = ctk.CTkLabel(self, text="Password:", font=("Arial", 14))
        password_label.pack(pady=(10, 0))
        self.password_entry = ctk.CTkEntry(self, width=250, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        login_button = ctk.CTkButton(self, text="Login", command=self.login_action)
        login_button.pack(pady=20)

        # Error Label
        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.pack()

    def login_action(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        role = self.validate_credentials(email, password)

        if role == "admin":
            self.destroy()
            from admin_page import AdminPage
            AdminPage()
        elif role == "user":
            self.destroy()
            from user_page import UserPage
            UserPage(email)
        else:
            self.error_label.configure(text="Invalid Email or Password!")

    def validate_credentials(self, email, password):
        try:
            with open("credentials.txt", "r") as file:
                for line in file:
                    role, stored_email, stored_password = line.strip().split("|")
                    if stored_email == email and stored_password == password:
                        return role
        except FileNotFoundError:
            self.error_label.configure(text="Credentials file not found!")
        return None