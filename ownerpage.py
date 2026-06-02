import customtkinter as i
import loginpage
import siginpage
import json as j

exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"
class owner:
    def __init__(self,master):
        self.master= master
       

        self.text=i.CTkLabel(self.master,text="ownerpage")
        self.text.pack()
        self.resturant_button= i.CTkButton(self.master,width=100,height=20,text="add/change resturant name")
        self.resturant_button.pack(pady=10)

        self.menue_b= i.CTkFrame(self.master)
        self.menue_b.pack(pady=20)
        self.a= i.CTkButton(self.menue_b,width=20,height=20,text="check",  command= self.checking)
        self.a.pack(side="left",pady=10)
        self.b= i.CTkButton(self.menue_b,width=20,height=20,text="add/change resturant name")
        self.b.pack(side="left",pady=20)
    def checking(self):
        with open(exact_path,'r')as f:
            data= j.load(f)
        l= loginpage.user.get_owner_resturant()
        s= siginpage.siginpage.get_owner_resturant
        if l:
            a=data[l]
            print("from login")
        else:
            a=data[s]
            print("form signin")
        print(a)
        


       



"""""
class owner:
    def __init__(self, master):
        self.master = master
        self.master.pack(fill="both", expand=True)

        self.text = i.CTkLabel(self.master, text="ownerpage")
        self.text.pack(pady=10)
        
        # 1. Build ONE invisible Mini-Box for all 4 buttons
        self.button_grid_box = i.CTkFrame(self.master, fg_color="transparent")
        self.button_grid_box.pack(pady=20)
        
        # --- ROW 0 (The Top Two Buttons) ---
        self.btn_1 = i.CTkButton(self.button_grid_box, text="Top Left")
        self.btn_1.grid(row=0, column=0, padx=10, pady=10)

        self.btn_2 = i.CTkButton(self.button_grid_box, text="Top Right")
        self.btn_2.grid(row=0, column=1, padx=10, pady=10)

        # --- ROW 1 (The Bottom Two Buttons) ---
        self.btn_3 = i.CTkButton(self.button_grid_box, text="Bottom Left")
        self.btn_3.grid(row=1, column=0, padx=10, pady=10)

        self.btn_4 = i.CTkButton(self.button_grid_box, text="Bottom Right")
        self.btn_4.grid(row=1, column=1, padx=10, pady=10)

        """