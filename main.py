import customtkinter as i
import loginpage as login
import retaurant1 as res
import json as j
import siginpage as sigin
import ys 


exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"

root= i.CTk()
root.iconbitmap('MHY.ico')
 # light brown light
login1= i.CTkFrame(root,fg_color="#fefae0")
signin= i.CTkFrame(root,fg_color="#fefae0")
resturantpage= i.CTkFrame(root,fg_color="#fefae0")
ooo= i.CTkFrame(root,fg_color="#fefae0")
oo= i.CTkFrame(root,fg_color="#fefae0")

resfrence_ow=res.thebackbone(ooo)
resfrence_ys= ys.AppController(oo)
i.set_appearance_mode("light")
i.set_default_color_theme("blue")
root.geometry('700x500')
root.title("MHY") #mahmoud hassen youssef
# add it to be able to close the page with esc button
root.bind("<Escape>", lambda event: root.destroy())

with open(exact_path,"r")as f:
    data=j.load(f)



login.user(login1,data["customer"],data["owner"],resfrence_ys,signin,resfrence_ow)
sigin.sb(signin,resfrence_ys,resfrence_ow)







root.mainloop()