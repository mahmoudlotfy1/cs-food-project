import customtkinter as i
import loginpage as usr
import returantpage as o
import json as j
import siginpage as ss


exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"

root= i.CTk()
login1= i.CTkFrame(root)
signin= i.CTkFrame(root)
resturantpage= i.CTkFrame(root)

i.set_appearance_mode("light")
i.set_default_color_theme("blue")
root.geometry('700x700')

with open(exact_path,"r")as f:
    data=j.load(f)



resturantname=["n","m","q","h","k"]

usr.user(login1,data["namepassword"],resturantpage,signin)
o.b(resturantpage,resturantname) 
ss.Newuser(signin,data["namepassword"],resturantpage)





root.mainloop()