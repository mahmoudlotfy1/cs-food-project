import customtkinter as i
import json as j

exact_path = r"c:\Users\mahmoud lotfy\Desktop\aalen uni\program\project\cs-food-project\uses.json"

class siginpage:
    def __init__(self,master,customerpage,ownerpage):
        self.master= master
        self.ow= i.CTkFrame(self.master)
        self.co= i.CTkFrame(self.master)
        
        #did get the self.owner/customer
        self.owner()
        self.customer()

        self.ownerpage= ownerpage
        self.cspage=customerpage
    def owner(self):
        
      # name par
        self.inputbarn=i.CTkEntry(self.ow,placeholder_text="name",width=200,height=20)
        # password par
        self.inputbarp=i.CTkEntry(self.ow,placeholder_text="password",width=200,height=20)
        self.inputbarn.pack(pady=20)
        self.inputbarp.pack(pady=21)
        #approve button
        self.buttono= i.CTkButton(self.ow,width=200,text="welcome",command=self.enteringowner)
        self.buttono.pack(pady=22)
           
         
    def enteringowner(self):
        with open(exact_path,"r")as f:
            data=j.load(f)
        data["owner"][self.inputbarn.get()]=self.inputbarp.get()
        data[self.inputbarn.get()]={"Resturant name": ""}
        self.ownerpage.x = self.inputbarn.get()
        with open(exact_path,"w")as f:
            j.dump(data,f,indent=4)
        self.master.pack_forget()
        self.ownerpage.master.pack(fill="both",expand=True)
    def customer(self):
    
        self.inputbarnn=i.CTkEntry(self.co,placeholder_text="name",width=200,height=20)
        self.inputbarpp=i.CTkEntry(self.co,placeholder_text="password",width=200,height=20)
        self.inputbarnn.pack(pady=20)
        self.inputbarpp.pack(pady=21)
        self.buttono= i.CTkButton(self.co,width=200,text="welcome",command=self.enteringcustomer)
        self.buttono.pack(pady=22)
          
    def enteringcustomer(self):
        with open(exact_path,"r")as f:
            data=j.load(f)
        data["customer"][self.inputbarnn.get()]=self.inputbarpp.get()
        with open(exact_path,"w")as f:
            j.dump(data,f,indent=4)
        self.master.pack_forget()
        self.cspage.show_home()
    def switch(self,text):
        self.co.pack_forget()
        self.ow.pack_forget()

        if text=="customer":
            self.co.pack(pady=20)
        if text=="owner":
            self.ow.pack(pady=20)
    
        
class sb(siginpage):
    def __init__(self,master,customerpage,ownerpage):
        super().__init__(master,customerpage,ownerpage)

        
        self.oandwpage= i.CTkSegmentedButton(self.master,values=["owner","customer"],command=self.switch ,width=100,height=10)
        self.oandwpage.pack(pady=10)
        self.oandwpage.set("customer")
        self.switch("customer")