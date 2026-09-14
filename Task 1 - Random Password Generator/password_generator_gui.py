import tkinter as tk
import secrets
import string
import pyperclip

window = tk.Tk()

window.title("Random Password Generator")
window.geometry("500x550")

length_label = tk.Label(window, text="Password Length:")
length_label.pack()

length_spinbox = tk.Spinbox(window, from_=8, to=50, width=10)
length_spinbox.pack()

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()
exclude_ambiguous_var = tk.BooleanVar()
history = []

tk.Checkbutton(
    window,
    text="Uppercase Letters",
    variable=uppercase_var
).pack()

tk.Checkbutton(
    window,
    text="Lowercase Letters",
    variable=lowercase_var
).pack()

tk.Checkbutton(
    window,
    text="Numbers",
    variable=numbers_var
).pack()

tk.Checkbutton(
    window,
    text="Symbols",
    variable=symbols_var
).pack()

tk.Checkbutton(
    window,
    text="Exclude ambiguous characters (0, O, l, 1)",
    variable=exclude_ambiguous_var
).pack()


def generate_password():
    length = int(length_spinbox.get())

    selected_types = sum([
        uppercase_var.get(),
        lowercase_var.get(),
        numbers_var.get(),
        symbols_var.get()
    ])

    if selected_types < 2:
        password_label.config(
            text="Please select at least 2 character types."
        )
        return

    characters = ""

    if uppercase_var.get():
        characters += string.ascii_uppercase

    if lowercase_var.get():
        characters += string.ascii_lowercase

    if numbers_var.get():
        characters += string.digits

    if symbols_var.get():
        characters += string.punctuation

    if exclude_ambiguous_var.get():
        characters = characters.translate(
            str.maketrans("", "", "0Ol1")
        )

    password = ""

    if uppercase_var.get():
        uppercase = string.ascii_uppercase
        if exclude_ambiguous_var.get():
            uppercase = uppercase.translate(
            str.maketrans("", "", "O")
        )
        
        password += secrets.choice(uppercase)

    if lowercase_var.get():
        lowercase = string.ascii_lowercase
        if exclude_ambiguous_var.get():
            lowercase = lowercase.translate(
            str.maketrans("", "", "l")
        )
        
        password += secrets.choice(lowercase)

    if numbers_var.get():
        numbers = string.digits
        if exclude_ambiguous_var.get():
            numbers = numbers.translate(
            str.maketrans("", "", "01")
        )
        
        password += secrets.choice(numbers)

    if symbols_var.get():
        symbols = string.punctuation
        
        password += secrets.choice(symbols)

    while len(password) < length:
        password += secrets.choice(characters)

    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)

    history.insert(0, password)

    if len(history) > 5:
        history.pop()

    history_listbox.delete(0, tk.END)

    for item in history:
        history_listbox.insert(tk.END, item)    

    strength = ""

    if length >= 12 and selected_types >= 3:
        strength = "Strong"
    elif length >= 10 and selected_types >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    password_label.config(
        text=f"{password}\nStrength: {strength}"
    )

generate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password
)

generate_button.pack()

password_label = tk.Label(
    window,
    text="Your password will appear here"
)

password_label.pack()

history_label = tk.Label(
    window,
    text="Generation History (Last 5)"
)

history_label.pack()

history_listbox = tk.Listbox(
    window,
    width=35,
    height=5
)

history_listbox.pack()

copy_button = tk.Button(
    window,
    text="Copy to Clipboard",
    command=lambda: pyperclip.copy(password_label.cget("text").split("\n")[0])
)

copy_button.pack()

window.mainloop()