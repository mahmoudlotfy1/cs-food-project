import customtkinter as i
import loginpage as usr
import retaurant1 as res
import json as j
import siginpage as ss

import ownerpage as ownerp
import ys 


exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"

root= i.CTk()
login1= i.CTkFrame(root)
signin= i.CTkFrame(root)
resturantpage= i.CTkFrame(root)
ooo= i.CTkFrame(root)
oo= i.CTkFrame(root)
# pass by refrence we use qqq to show ooo belonge to ownerpage
resfrence_ow=res.thebackbone(ooo)
resfrence_ys= ys.AppController(oo)
i.set_appearance_mode("light")
i.set_default_color_theme("blue")
root.geometry('700x700')

with open(exact_path,"r")as f:
    data=j.load(f)



usr.user(login1,data["customer"],data["owner"],resfrence_ys,signin,resfrence_ow)
ss.sb(signin,resfrence_ys,resfrence_ow)







root.mainloop()