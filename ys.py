import json
import customtkinter as ctk
from recipt1 import main_rc
DB_FILE = "db.json"




class DataManager:
    def load(self):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"restaurants": []}
            with open(DB_FILE, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
            return data
    def get_restaurants(self):
        data = self.load()
        return data.get("restaurants", [])


class CartManager:
    def __init__(self):
        self.items = []

    def add(self, dish, restaurant):
        self.items.append({**dish, "from": restaurant})

    def total(self):
        return sum(float(item["price"]) for item in self.items)
    def clear(self):
        self.items = []

    





class HomePage(ctk.CTkFrame):
    def __init__(self, controller):
        super().__init__(controller.root)
        self.controller = controller
        
        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(top_frame, text="Restaurants", font=("Arial", 18)).pack(side="left")
        
        cart_text = f"Cart ({len(controller.cart.items)})"
        ctk.CTkButton(top_frame, text=cart_text, fg_color="#606c38", hover_color="#283618",command=controller.show_cart).pack(side="right")
        
        scroll_frame = ctk.CTkScrollableFrame(self, height=400)
        scroll_frame.pack(fill="both", expand=True, padx=10)
        
        for restaurant in controller.data.get_restaurants():
            ctk.CTkButton(
                scroll_frame, 
                text=restaurant["name"], fg_color="#606c38", hover_color="#283618",
                command=lambda r=restaurant: controller.show_dishes(r)
            ).pack(fill="x", pady=3)


class AppController:
    def __init__(self,master):
        self.root = master
        
      
        
        self.data = DataManager()
        self.cart = CartManager()
        self.current_frame = None
        
        
      
        

    def switch_frame(self, new_frame):
        if self.current_frame:
            self.current_frame.pack_forget()
            self.current_frame.destroy()
            
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)

    def show_home(self):
      self.root.pack(fill="both", expand=True)
      self.switch_frame(HomePage(self))
               
    def show_dishes(self, restaurant):
        frame = ctk.CTkFrame(self.root)
        
        ctk.CTkButton(
            frame, 
            text="← Back", fg_color="#606c38", hover_color="#283618",
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
                fg_color="#606c38", hover_color="#283618",
                command=lambda d=dish: self.cart.add(d, restaurant["name"])
            ).pack(side="right", padx=5)
            
        self.switch_frame(frame)

    def show_cart(self):
        frame = ctk.CTkFrame(self.root)
        ctk.CTkButton(frame, text="← Back", fg_color="#606c38", hover_color="#283618",command=lambda: self.switch_frame(HomePage(self))).pack(pady=5)
        scroll = ctk.CTkScrollableFrame(frame, height=350); scroll.pack(fill="both", expand=True, padx=10)
        for item in self.cart.items:
            ctk.CTkLabel(scroll, text=f"{item['name']} — ${item['price']} ({item['from']})").pack(anchor="w", pady=2)
        ctk.CTkLabel(frame, text=f"Total: ${self.cart.total():.2f}", font=("Arial", 15)).pack(pady=5)
        #process_checkout
        def process_checkout():
            final_items= list(self.cart.items)
            # it saves the items
            final_total = self.cart.total()
            if len(final_items) > 0:
                # it is created by jo to clean the cart
                self.cart.clear()
                
                self.switch_frame(main_rc(self, final_items, final_total))
            else:
                print("Cart is empty!")
                # the comand
        self.checkout_b = ctk.CTkButton(frame, text="Checkout", fg_color="#606c38", hover_color="#283618",command=process_checkout)
        self.checkout_b.pack(pady=10)
        self.switch_frame(frame)

