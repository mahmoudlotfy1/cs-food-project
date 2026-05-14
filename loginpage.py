import customtkinter as i

#login is master
class starting:
    def __init__(self,login,name,net,s):
        self.name=name
        self.s=s
        self.login= login
        self.next=net
        self.login.pack(fill="both", expand= True)

        self.text=i.CTkLabel(login,text="Hi")
        self.text.pack(pady=7)
        self.username= i.CTkEntry(login,placeholder_text="name pls",width=200)
        self.username.pack(pady=10)
        self.userpassword= i.CTkEntry(login,placeholder_text="name pls",width=200)
        self.userpassword.pack(pady=12)
        

class user(starting):
    def __init__(self, login, name, net,s):
        super().__init__(login, name,net,s)
        self.singin=False
        self.b = i.CTkButton(login,text="login",fg_color="white",width=200,command= self.loging)
        self.b.pack(pady=14)
        self.b = i.CTkButton(login,text="siginup",fg_color="blue",width=200,command= self.loging)
        self.b.pack(pady=17)

    def loging(self):
        if self.singin==False:
            self.singin= True
            self.login.pack_forget()
            self.s.pack(fill="both", expand= True) 
            

        if self.username.get() in self.name and  self.userpassword.get() in self.name[self.username.get()]:
            self.login.pack_forget()
            self.next.pack(fill="both", expand= True) 
            

        
    

