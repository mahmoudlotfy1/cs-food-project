import customtkinter as i


class st:
    # the information we need (master: new page using frame, name_cs: customer name for json data
    # name_ow owner name from json data, ys: customer page youssef, s sigin page,ownerpage resturant page)
    def __init__(self,master,name_cs,name_ow,ys,s,ownerpage):
        # define using self
        self.name_cs=name_cs
        self.name_ow= name_ow
        self.ownerpage= ownerpage
        self.s=s
        self.login= master
        self.next=ys
        self.login.pack(fill="both", expand= True)
        # label the welcome text 
        self.text=i.CTkLabel(master,text="Welcome", font=("",56))
        self.text.pack(pady=10)
        # entery name placeholder_text the transpance text
        self.username= i.CTkEntry(master,placeholder_text="name pls",width=200)
        self.username.pack(pady=10)
        self.userpassword= i.CTkEntry(master,placeholder_text="password pls",width=200,show="lol")
        self.userpassword.pack(pady=12)
        

class user(st):
    def __init__(self,master,name_cs,name_ow,ys,s,ownerpage):
        # the inheratense
        super().__init__(master,name_cs,name_ow,ys,s,ownerpage)
        self.singin=False
        # self.b the button  for loging in
        self.b = i.CTkButton(master,text="login",width=200,command= self.loging)
        self.b.pack(pady=14)
        # for singin 
        self.b = i.CTkButton(master,text="signup",width=200,command= self.singinn)
        self.b.pack(pady=17)

    def loging(self):
        #get grab the name and the password from those verables
        # if the name that was give is avalible in the customer data show us the log in  customer page
        if self.username.get() in self.name_cs and  self.userpassword.get() in self.name_cs[self.username.get()]:
            
            self.login.pack_forget()
            self.next.show_home() 
        # if the name that was give is avalible in the owner data show us the log in  owner page
        if self.username.get() in self.name_ow and  self.userpassword.get() in self.name_ow[self.username.get()]:
            self.ownerpage.x = self.username.get()
            self.login.pack_forget()
            self.ownerpage.master.pack(fill="both", expand= True) 
        
        # doesn't exist
        else: 
            if self.username.get() not in self.name_cs and self.username.get() not in self.name_ow:
                print("something is messing")
    # if the sign in button pressed the false turn true
    def singinn(self):
        if self.singin==False:
              self.singin= True
              self.login.pack_forget()
              self.s.pack(fill="both", expand= True) 
    
        
            
          
            

        
            

        
    

