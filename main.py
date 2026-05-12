import customtkinter as i
import loginpage as usr
import returantpage as o
root= i.CTk()
login1= i.CTkFrame(root)
resturantpage= i.CTkFrame(root)
i.set_appearance_mode("light")
i.set_default_color_theme("blue")
root.geometry('700x700')

savedname= ["mmm","hi"]
resturantname=["n","m","q","h","k"]

usr.user(login1,savedname[0],savedname[1],resturantpage)
o.b(resturantpage,resturantname)





root.mainloop()