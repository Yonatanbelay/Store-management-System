from tkinter import *
from login import LoginPage

class AdminPage:
    def __init__(self):
        self.display = Tk()
        self.display.title("Admin Page")
        self.display.minsize(600, 500)
        self.display.config(background="#B0B0B0")
        self.setup_ui()
        self.display.mainloop()

    # Sets up the UI
    def setup_ui(self):
        Button(self.display, text="Log Out", bg="red", fg="white", font=("Helvetica", 12, 'bold'), relief="raised",
               command=self.logout).place(x=10, y=10)

        Label(self.display, text="Admin Dashboard", font=("Helvetica", 20, 'bold'), bg="#f4f6f7",
              fg="#4CAF50").pack(pady=20)

        inventory_frame = Frame(self.display, bg="#ffffff", relief="solid", bd=2, padx=20, pady=20)
        inventory_frame.pack(pady=20, padx=20, fill="x")
        Label(inventory_frame, text="Inventory Management", font=("Helvetica", 16, 'bold'), bg="#ffffff",
              fg="#4CAF50").pack(pady=10)
        Button(inventory_frame, text="Add Material", command=self.add_material, width=20, relief="raised", bg="#4CAF50",
               fg="white", font=("Helvetica", 12)).pack(pady=5)
        Button(inventory_frame, text="Update Material", command=self.update_material, width=20, relief="raised",
               bg="#FF9800", fg="white", font=("Helvetica", 12)).pack(pady=5)
        Button(inventory_frame, text="Remove Material", command=self.remove_material, width=20, relief="raised",
               bg="#F44336", fg="white", font=("Helvetica", 12)).pack(pady=5)
        Button(inventory_frame, text="Show All Inventory", command=self.show_all_inventory, width=20, relief="raised",
               bg="#2196F3", fg="white", font=("Helvetica", 12)).pack(pady=10)

        user_frame = Frame(self.display, bg="#ffffff", relief="solid", bd=2, padx=20, pady=20)
        user_frame.pack(pady=20, padx=20, fill="x")
        Label(user_frame, text="User Management", font=("Helvetica", 16, 'bold'), bg="#ffffff",
              fg="#4CAF50").pack(pady=10)
        Button(user_frame, text="Add User", command=self.add_user, width=20, relief="raised", bg="#4CAF50", fg="white",
               font=("Helvetica", 12)).pack(pady=5)
        Button(user_frame, text="Remove User", command=self.remove_user, width=20, relief="raised", bg="#F44336",
               fg="white", font=("Helvetica", 12)).pack(pady=5)

    # Logs out the admin and opens the login page
    def logout(self):
        self.display.destroy()
        LoginPage()

    # Modifies the accounts in the credentials file
    def modify_credentials(self, email, remove=False):
        with open("credentials.txt", "r") as file:
            lines = file.readlines()
        with open("credentials.txt", "w") as file:
            for line in lines:
                if email not in line or not remove:
                    file.write(line)

    # Modifies the inventory in the inventory file
    def modify_inventory(self, name, quantity=None, remove=False):
        with open("inventory.txt", "r") as file:
            lines = file.readlines()
        with open("inventory.txt", "w") as file:
            for line in lines:
                item, qty = line.strip().split("|")
                if item != name:
                    file.write(line)
                elif not remove:
                    file.write(f"{name}|{quantity}\n")

    # Adds a new user
    def add_user(self):
        self.manage_users("add")

    # Removes an existing user
    def remove_user(self):
        self.manage_users("remove")

    # Manages user actions (add/remove)
    def manage_users(self, action):
        top = Toplevel(self.display)
        top.title("Manage Users")
        top.config(bg="#f4f6f7")
        top.geometry("400x300")

        Label(top, text="Email:", font=("Helvetica", 12), bg="#f4f6f7", fg="#333").pack(pady=10)
        email_entry = Entry(top, width=40, font=("Helvetica", 12))
        email_entry.pack(pady=5)

        Label(top, text="Password:", font=("Helvetica", 12), bg="#f4f6f7", fg="#333").pack(pady=10)
        password_entry = Entry(top, width=40, show="*", font=("Helvetica", 12))
        password_entry.pack(pady=5)

        def save_user():
            email = email_entry.get()
            password = password_entry.get()
            if action == "add":
                with open("credentials.txt", "a") as file:
                    file.write(f"user|{email}|{password}\n")
            elif action == "remove":
                self.modify_credentials(email, remove=True)
            top.destroy()

        Button(top, text="Submit", command=save_user, width=20, relief="raised", bg="#4CAF50", fg="white",
               font=("Helvetica", 12)).pack(pady=20)

    # Adds a new material to the inventory
    def add_material(self):
        self.manage_inventory("add")

    # Updates an existing material in the inventory
    def update_material(self):
        self.manage_inventory("update")

    # Removes a material from the inventory
    def remove_material(self):
        self.manage_inventory("remove")

    # Manages inventory actions (add/update/remove)
    def manage_inventory(self, action):
        top = Toplevel(self.display)
        top.title("Manage Inventory")
        top.config(bg="#f4f6f7")
        top.geometry("400x300")

        Label(top, text="Material Name:", font=("Helvetica", 12), bg="#f4f6f7", fg="#333").pack(pady=10)
        name_entry = Entry(top, width=40, font=("Helvetica", 12))
        name_entry.pack(pady=5)

        Label(top, text="Quantity:", font=("Helvetica", 12), bg="#f4f6f7", fg="#333").pack(pady=10)
        quantity_entry = Entry(top, width=40, font=("Helvetica", 12))
        quantity_entry.pack(pady=5)

        def save_inventory():
            name = name_entry.get()
            quantity = quantity_entry.get()
            if action == "add":
                with open("inventory.txt", "a") as file:
                    file.write(f"{name}|{quantity}\n")
            elif action == "update":
                self.modify_inventory(name, quantity)
            elif action == "remove":
                self.modify_inventory(name, remove=True)
            top.destroy()

        Button(top, text="Submit", command=save_inventory, width=20, relief="raised", bg="#4CAF50", fg="white",
               font=("Helvetica", 12)).pack(pady=20)

    # Displays all the inventory in a new window
    def show_all_inventory(self):
        top = Toplevel(self.display)
        top.title("All Inventory")
        top.config(bg="#f4f6f7")
        top.geometry("600x500")

        Label(top, text="Inventory List", font=("Helvetica", 18, 'bold'), bg="#f4f6f7", fg="#4CAF50").pack(pady=20)

        canvas = Canvas(top, bg="#f4f6f7")
        scrollbar = Scrollbar(top, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        inventory_frame = Frame(canvas, bg="#f4f6f7")
        canvas.create_window((0, 0), window=inventory_frame, anchor="nw")

        try:
            with open("inventory.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    Label(inventory_frame, text="No inventory found", font=("Helvetica", 12), bg="#f4f6f7",
                          fg="#888").pack(pady=10)
                else:
                    row_count = 0
                    for line in lines:
                        name, qty = line.strip().split("|")
                        row_color = "#ffffff" if row_count % 2 == 0 else "#f1f1f1"
                        row_count += 1

                        row = Frame(inventory_frame, bg=row_color, pady=10, padx=15)
                        row.pack(fill="x", pady=5)
                        Label(row, text=f"Material: {name}", font=("Helvetica", 12), bg=row_color,
                              fg="#333", width=30, anchor="w").pack(side=LEFT)
                        Label(row, text=f"Quantity: {qty}", font=("Helvetica", 12), bg=row_color,
                              fg="#333", width=20, anchor="e").pack(side=RIGHT)

        except FileNotFoundError:
            Label(inventory_frame, text="No inventory file found", font=("Helvetica", 12), bg="#f4f6f7",
                  fg="#888").pack(pady=10)
        inventory_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
