
import customtkinter as ctk

def say_hello():
    print("Hello from the newly generated file!")

root = ctk.CTk()
root.geometry("200x200")

btn = ctk.CTkButton(root, text="Click Me", command=say_hello)
btn.pack(pady=50)

root.mainloop()
