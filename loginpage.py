import customtkinter as i
import returantpage as u

class starting:
    def __init__(self,login,name,password,net):
        self.name=name
        self.password=password
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
    def __init__(self, login, name, password,net):
        super().__init__(login, name, password,net)

        self.b = i.CTkButton(login,text="login",fg_color="white",width=200,command= self.loging)
        self.b.pack(pady=14)
    def loging(self):
        if self.username.get() == self.name and  self.userpassword.get()== self.password:
            self.login.pack_forget()
            self.next.pack(fill="both", expand= True)
            

        
    

