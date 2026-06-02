import customtkinter as i
import loginpage as usr
import returantpage as r
import json as j
import siginpage as ss
import mahmoudkoshary as mk
import hassendawla as hd
import youssefkabab as yk
import ownerpage as ownerp



exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"

root= i.CTk()
login1= i.CTkFrame(root)
signin= i.CTkFrame(root)
resturantpage= i.CTkFrame(root)
ooo= i.CTkFrame(root)
# pass by refrence we use qqq to show ooo belonge to ownerpage
resfrence_ow=ownerp.owner(ooo)
i.set_appearance_mode("light")
i.set_default_color_theme("blue")
root.geometry('700x700')

with open(exact_path,"r")as f:
    data=j.load(f)

mmk= i.CTkFrame(root)
ykk= i.CTkFrame(root)
hdd=i.CTkFrame(root)

mkrestaurant=mk.mahresturant(mmk)
ykrestaurant= yk.mahresturant(ykk)
hdrestaurant= hd.mahresturant(hdd)

resturantname={ "mahmoud": mmk,
               "youssef":ykk,
                "hassen":hdd }

usr.user(login1,data["customer"],data["owner"],resturantpage,signin,ooo)
r.b(resturantpage,resturantname) 
ss.sb(signin,resturantpage,ooo)







root.mainloop()