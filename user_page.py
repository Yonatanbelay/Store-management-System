from tkinter import *
from login import LoginPage

class UserPage:
    def __init__(self, email):
        self.email = email
        self.display = Tk()
        self.display.title("User Dashboard")
        self.display.minsize(600, 500)
        self.display.config(bg="#B0B0B0")
        self.setup_ui()
        self.display.mainloop()

    # Sets up the UI
    def setup_ui(self):
        Button(self.display, text="Log Out", bg="red", fg="white", font=("Helvetica", 12, 'bold'), relief="raised",
               command=self.logout).place(x=10, y=10)

        (Label(self.display, text=f"Welcome, {self.email.split('@')[0].title()}", font=("Helvetica", 20, 'bold'), bg="#f4f6f7", fg="#4CAF50").
         pack(pady=20))

        inventory_frame = Frame(self.display, bg="#ffffff", relief="solid", bd=2, padx=20, pady=20)
        inventory_frame.pack(pady=20, padx=20, fill="x")
        Label(inventory_frame, text="Inventory Access", font=("Helvetica", 16, 'bold'), bg="#ffffff",
              fg="#4CAF50").pack(pady=10)
        Button(inventory_frame, text="View Inventory", command=self.view_inventory, width=20, relief="raised",
               bg="#4CAF50", fg="white", font=("Helvetica", 12)).pack(pady=5)

        material_frame = Frame(self.display, bg="#ffffff", relief="solid", bd=2, padx=20, pady=20)
        material_frame.pack(pady=20, padx=20, fill="x")
        Label(material_frame, text="Material Management", font=("Helvetica", 16, 'bold'), bg="#ffffff",
              fg="#4CAF50").pack(pady=10)
        Button(material_frame, text="Add/Update Material", command=self.add_update_material, width=20, relief="raised",
               bg="#FF9800", fg="white", font=("Helvetica", 12)).pack(pady=5)

    # Logs out the user and opens the login page
    def logout(self):
        self.display.destroy()
        LoginPage()

    # Displays the inventory in a new window
    def view_inventory(self):
        top = Toplevel(self.display)
        top.title("View Inventory")
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
                        Label(row, text=f"Material: {name}", font=("Helvetica", 12), bg=row_color, fg="#333", width=30,
                              anchor="w").pack(side=LEFT)
                        Label(row, text=f"Quantity: {qty}", font=("Helvetica", 12), bg=row_color, fg="#333", width=20,
                              anchor="e").pack(side=RIGHT)

        except FileNotFoundError:
            Label(inventory_frame, text="No inventory file found", font=("Helvetica", 12), bg="#f4f6f7",
                  fg="#888").pack(pady=10)

        inventory_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # Opens a window to add or update material
    def add_update_material(self):
        top = Toplevel(self.display)
        top.title("Add/Update Material")
        top.config(bg="#f4f6f7")
        top.geometry("400x300")

        Label(top, text="Material Name:", font=("Helvetica", 12), bg="#f4f6f7", fg="#333").pack(pady=10)
        name_entry = Entry(top, width=40, font=("Helvetica", 12))
        name_entry.pack(pady=5)

        Label(top, text="Quantity:", font=("Helvetica", 12), bg="#f4f6f7", fg="#333").pack(pady=10)
        quantity_entry = Entry(top, width=40, font=("Helvetica", 12))
        quantity_entry.pack(pady=5)

        def save_material():
            material_name = name_entry.get()
            quantity = quantity_entry.get()
            with open("user_assignments.txt", "a") as file:
                file.write(f"{self.email}|{material_name}|{quantity}\n")
            top.destroy()

        Button(top, text="Submit", command=save_material, width=20, relief="raised", bg="#4CAF50", fg="white",
               font=("Helvetica", 12)).pack(pady=20)
