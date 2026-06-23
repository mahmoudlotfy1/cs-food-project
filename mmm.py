import customtkinter as ctk
import json

DB = "db.json"

class DataManager:
    def load(self):
        try:
            return json.load(open(DB))
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"users": [], "restaurants": []}
            json.dump(data, open(DB, "w"))
            return data

    def get_user(self, u, p):
        for user in self.load()["users"]:
            if user["username"] == u and user["password"] == p and user["role"] == "customer":
                return user
        return None

    def get_restaurants(self):
        return self.load()["restaurants"]

class CartManager:
    def __init__(self): self.items = []
    def add(self, dish, restaurant): self.items.append({**dish, "from": restaurant})
    def total(self): return sum(i["price"] for i in self.items)
    def clear(self): self.items = []

class LoginPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller.root)
        self.controller = controller
        ctk.CTkLabel(self, text="Login", font=("Arial", 20)).pack(pady=10)
        self.u = ctk.CTkEntry(self, placeholder_text="Username"); self.u.pack(pady=5)
        self.p = ctk.CTkEntry(self, placeholder_text="Password", show="*"); self.p.pack(pady=5)
        self.msg = ctk.CTkLabel(self, text=""); self.msg.pack()
        ctk.CTkButton(self, text="Login", command=self.login).pack(pady=10)

    def login(self):
        user = self.controller.data.get_user(self.u.get(), self.p.get())
        if user: self.controller.show_home(user["username"])
        else: self.msg.configure(text="Invalid credentials", text_color="red")

class HomePage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller.root)
        self.controller = controller
        top = ctk.CTkFrame(self); top.pack(fill="x", padx=10, pady=5)
        ctk.CTkLabel(top, text="Restaurants", font=("Arial", 18)).pack(side="left")
        ctk.CTkButton(top, text=f"Cart ({len(controller.cart.items)})", command=controller.show_cart).pack(side="right")
        scroll = ctk.CTkScrollableFrame(self, height=400); scroll.pack(fill="both", expand=True, padx=10)
        for r in controller.data.get_restaurants():
            ctk.CTkButton(scroll, text=r["name"], command=lambda r=r: controller.show_dishes(r)).pack(fill="x", pady=3)

class AppController:
    def __init__(self):
        self.root = ctk.CTk(); self.root.title("FoodApp"); self.root.geometry("400x500")
        self.data = DataManager(); self.cart = CartManager()
        self.current = None
        self.login_page = LoginPage(self); self.login_page.pack(fill="both", expand=True)
        self.root.mainloop()

    def switch(self, new_frame):
        if self.current: self.current.pack_forget(); self.current.destroy()
        self.current = new_frame; new_frame.pack(fill="both", expand=True)

    def show_home(self, username):
        if hasattr(self, 'login_page'): self.login_page.pack_forget()
        self.switch(HomePage(self))

    def show_dishes(self, restaurant):
        frame = ctk.CTkFrame(self.root); scroll = ctk.CTkScrollableFrame(frame, height=380); scroll.pack(fill="both", expand=True, padx=10)
        ctk.CTkButton(frame, text="← Back", command=lambda: self.switch(HomePage(self))).pack(pady=5)
        for dish in restaurant["dishes"]:
            row = ctk.CTkFrame(scroll); row.pack(fill="x", pady=4, padx=5)
            ctk.CTkLabel(row, text=f"{dish['name']}  ${dish['price']}", font=("Arial", 13)).pack(side="left", padx=8)
            ctk.CTkButton(row, text="Add", width=60, command=lambda d=dish: self.cart.add(d, restaurant["name"])).pack(side="right", padx=5)
        self.switch(frame)

    def show_cart(self):
        frame = ctk.CTkFrame(self.root)
        ctk.CTkButton(frame, text="← Back", command=lambda: self.switch(HomePage(self))).pack(pady=5)
        scroll = ctk.CTkScrollableFrame(frame, height=350); scroll.pack(fill="both", expand=True, padx=10)
        for item in self.cart.items:
            ctk.CTkLabel(scroll, text=f"{item['name']} — ${item['price']} ({item['from']})").pack(anchor="w", pady=2)
        ctk.CTkLabel(frame, text=f"Total: ${self.cart.total():.2f}", font=("Arial", 15)).pack(pady=5)
        ctk.CTkButton(frame, text="Checkout", command=lambda: [self.cart.clear(), self.switch(HomePage(self))]).pack()
        self.switch(frame)

AppController()