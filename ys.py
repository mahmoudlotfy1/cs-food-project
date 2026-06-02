import json
import customtkinter as ctk

DB_FILE = "db.json"

class DataManager:
    def load(self):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"users": [], "restaurants": []}
            with open(DB_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            return data

    def get_user(self, username, password):
        data = self.load()
        for user in data.get("users", []):
            if (user.get("username") == username and 
                user.get("password") == password and 
                user.get("role") == "customer"):
                return user
        return None

    def get_restaurants(self):
        data = self.load()
        return data.get("restaurants", [])


class CartManager:
    def __init__(self):
        self.items = []

    def add(self, dish, restaurant):
        self.items.append({**dish, "from": restaurant})

    def total(self):
        return sum(item["price"] for item in self.items)

    def clear(self):
        self.items = []


class LoginPage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller.root)
        self.controller = controller
        
        ctk.CTkLabel(self, text="Login", font=("Arial", 20)).pack(pady=10)
        
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(pady=5)
        
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=5)
        
        self.msg_label = ctk.CTkLabel(self, text="")
        self.msg_label.pack()
        
        ctk.CTkButton(self, text="Login", command=self.login).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.controller.data.get_user(username, password)
        
        if user:
            self.controller.show_home(user["username"])
        else:
            self.msg_label.configure(text="Invalid credentials", text_color="red")


class HomePage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller.root)
        self.controller = controller
        
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(top_frame, text="Restaurants", font=("Arial", 18)).pack(side="left")
        
        cart_text = f"Cart ({len(controller.cart.items)})"
        ctk.CTkButton(top_frame, text=cart_text, command=controller.show_cart).pack(side="right")
        
        scroll_frame = ctk.CTkScrollableFrame(self, height=400)
        scroll_frame.pack(fill="both", expand=True, padx=10)
        
        for restaurant in controller.data.get_restaurants():
            ctk.CTkButton(
                scroll_frame, 
                text=restaurant["name"], 
                command=lambda r=restaurant: controller.show_dishes(r)
            ).pack(fill="x", pady=3)


class AppController:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("FoodApp")
        self.root.geometry("400x500")
        
        self.data = DataManager()
        self.cart = CartManager()
        self.current_frame = None
        
        self.login_page = LoginPage(self)
        self.login_page.pack(fill="both", expand=True)
        
        self.root.mainloop()

    def switch_frame(self, new_frame):
        if self.current_frame:
            self.current_frame.pack_forget()
            self.current_frame.destroy()
            
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def show_home(self, username):
        if hasattr(self, 'login_page') and self.login_page.winfo_exists():
            self.login_page.pack_forget()
            
        self.switch_frame(HomePage(self))

    def show_dishes(self, restaurant):
        frame = ctk.CTkFrame(self.root)
        
        ctk.CTkButton(
            frame, 
            text="← Back", 
            command=lambda: self.switch_frame(HomePage(self))
        ).pack(pady=5)
        
        scroll_frame = ctk.CTkScrollableFrame(frame, height=380)
        scroll_frame.pack(fill="both", expand=True, padx=10)
        
        for dish in restaurant.get("dishes", []):
            row = ctk.CTkFrame(scroll_frame)
            row.pack(fill="x", pady=4, padx=5)
            
            dish_text = f"{dish['name']}  ${dish['price']}"
            ctk.CTkLabel(row, text=dish_text, font=("Arial", 13)).pack(side="left", padx=8)
            
            ctk.CTkButton(
                row, 
                text="Add", 
                width=60, 
                command=lambda d=dish: self.cart.add(d, restaurant["name"])
            ).pack(side="right", padx=5)
            
        self.switch_frame(frame)

    def show_cart(self):
        frame = ctk.CTkFrame(self.root)
        
        ctk.CTkButton(
            frame, 
            text="← Back", 
            command=lambda: self.switch_frame(HomePage(self))
        ).pack(pady=5)
        
        scroll_frame = ctk.CTkScrollableFrame(frame, height=350)
        scroll_frame.pack(fill="both", expand=True, padx=10)
        
        for item in self.cart.items:
            item_text = f"{item['name']} — ${item['price']} ({item['from']})"
            ctk.CTkLabel(scroll_frame, text=item_text).pack(anchor="w", pady=2)
            
        total_text = f"Total: ${self.cart.total():.2f}"
        ctk.CTkLabel(frame, text=total_text, font=("Arial", 15)).pack(pady=5)
        
        def checkout():
            self.cart.clear()
            self.switch_frame(HomePage(self))
            
        ctk.CTkButton(frame, text="Checkout", command=checkout).pack()
        
        self.switch_frame(frame)

if __name__ == "__main__":
    AppController()