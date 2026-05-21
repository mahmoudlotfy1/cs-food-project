# 1. Write the code you want in the new file as a giant String
my_new_code = """
import customtkinter as ctk

def say_hello():
    print("Hello from the newly generated file!")

root = ctk.CTk()
root.geometry("200x200")

btn = ctk.CTkButton(root, text="Click Me", command=say_hello)
btn.pack(pady=50)

root.mainloop()
"""

# 2. Open a brand new file ending in .py using "w" (Bulldozer mode)
with open("generated_app.py", "w") as f:
    
    # 3. Write your giant string into the file!
    f.write(my_new_code)

print("Check your folder! generated_app.py was just built.")




resturantname={ "mahmoud": "mkrestaurant",
               "youssef":"ykrestaurant",
                "hassen":"hdrestaurant" }

v= resturantname["mahmoud"]
print(v)

