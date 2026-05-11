import customtkinter as i


root = i.CTk()
i.set_appearance_mode("dark")
i.set_default_color_theme("blue")
root.geometry('500x500')


person= ["mahmoud", 1234]

class user():
    def __init__(self,name,password):
        self.name=name
        self.password= password
        
        self.lol=i.CTkEntry(root,placeholder_text="yoyo",width=100)
        self.lol.pack(padx=1, pady= 4)
        self.button= i.CTkButton(root, text="yoyo",width=100,command= self.yourmom)
        self.button.pack(pady=6)
    def yourmom(self):
        names= self.lol.get()
        if names == self.name:
            print("hi")
        else:
            print("noooommmm")


        


usr= user(person[0],person[1])
 
root.mainloop()