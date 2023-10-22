import tkinter as tk
import random
import string
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=False):
    # Define character sets based on complexity options
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Check if at least one character set is selected
    if not all_chars:
        raise ValueError(
            "At least one character set (lowercase, uppercase, digits, or special characters) must be selected.")

    # Generate the password
    password: str = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        result_label.config(text="Please fill out all fields.")
        return
    if not is_valid_email(email):
        result_label.config(text="Please check your e-mail.")
        return

    with open("data.txt", "a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        result_label.config(text="Password saved.")


def is_valid_email(email):
    if "@" in email and "." in email:
        return True
    return False


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

# Create a canvas for the logo
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels and Entry fields for website, email, and password
website_label = tk.Label(text="Website:")
email_label = tk.Label(text="Email/Username:")
password_label = tk.Label(text="Password:")
result_label = tk.Label(text="")

website_entry = tk.Entry(width=35)
email_entry = tk.Entry(width=35)
password_entry = tk.Entry(width=21)

# Buttons for generating passwords and adding entries
generate_password_button = tk.Button(text="Generate Password", width=15, command=generate_password)
add_button = tk.Button(text="Add", width=30, command=save_password)

# Grid layout for labels, entry fields, and buttons
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
result_label.grid(column=0, row=4)

website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

email_entry.insert(0, "@gmail.com")
website_entry.focus()
root.mainloop()
