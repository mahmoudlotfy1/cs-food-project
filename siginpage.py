import customtkinter as i
import json as j

exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"

class sigin:
    def __init__(self,master):
        
        self.master=master
        
        self.inputname= i.CTkEntry(self.master,placeholder_text="name pls",width=200)
        self.inputname.pack(pady=20)
        self.inputpass= i.CTkEntry(self.master,placeholder_text="password pls",width=200)
        self.inputpass.pack(pady=21)

class Newuser(sigin):
    def __init__(self, master,resturant):
        super().__init__(master)
        self.resturant=resturant
        self.b=i.CTkButton(self.master,text="welcome",fg_color="blue",command=self.saveuser)
        self.b.pack(pady=22)
    def saveuser(self):
        name=self.inputname.get()
        password= self.inputpass.get()
        


        with open(exact_path,"r")as f:
            data=j.load(f)
        
        data["namepassword"][name]=password
        
        
        
        with open(exact_path,"w")as f:
            j.dump(data,f)
        
        if name in data["namepassword"] and password== data["namepassword"][name]:
            self.master.pack_forget()
            self.resturant.pack(fill="both",expand=True)

           
            
        

        

