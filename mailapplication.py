import tkinter as tk
from tkinter import ttk

def send_email():
    # Placeholder function for sending email
    print("Email sent!")

# Create main window
root = tk.Tk()
root.title("Simple Mail App")

# Create and pack widgets
label_to = ttk.Label(root, text="To:")
label_to.pack()

entry_to = ttk.Entry(root)
entry_to.pack()

label_subject = ttk.Label(root, text="Subject:")
label_subject.pack()

entry_subject = ttk.Entry(root)
entry_subject.pack()

label_body = ttk.Label(root, text="Body:")
label_body.pack()

text_body = tk.Text(root, height=5, width=30)
text_body.pack()

button_send = ttk.Button(root, text="Send", command=send_email)
button_send.pack()

# Run the main loop
root.mainloop()
