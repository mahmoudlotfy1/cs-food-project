import customtkinter as c 
class user:
  def __init__(self, name, passwort):
    self.name=name
    self.passwort=passwort
  
class owner(user):
  def __init__(self,name, passwort):
    super().__init__(user.name, user.passwort)
class customer(user):
  def __init__(self,user.name, user.passwort):
    super().__init__(user.name, user.passwort)
class food_menu:
  def __init__(self, name):
    self.name=name
class dessert(food_menu):
  def __init__(self, name, passwort):
    super().__init__(name, passwort)
class drinks(food_menu):
  def __init__(self, name, passwort):
    super().__init__(name, passwort)
class maincourse(food_menu):
  def __init__(self, name, passwort):
    super().__init__(name, passwort)
class kids_menu(food_menu):
  def __init__(self, name, passwort):
    super().__init__(name, passwort)
class food_app(c.CTk):
    
    def login(self, user.name, user.passwort):
        if user.name=="admin" and user.passwort=="admin":
            print("Login successful!")
        else:
            print("Login failed!")
    def sign_up(self, user.name, user.passwort):
        self.name=user.name
        self.passwort=user.passwort
        print("Sign up successful!")
       
       
    def __init__(self):
        super().__init__()
           
        self.title("Food App")
        self.geometry("400x700")
        self.c.CTkLabel(self, text="Welcome to the Food App!").pack(pady=20, padx=20)
        self.c.CTkButton(self, text="Login", command=self.login).pack(pady=10, padx=20)
        self.c.CTkButton(self, text="Sign Up", command=self.sign_up).pack(pady=10, padx=20)
if __name__ == "__main__":

    app = food_app()
    app.mainloop()