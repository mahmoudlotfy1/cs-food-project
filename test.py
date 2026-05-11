import customtkinter as ctk

# ================= 1. Data Models =================
class MenuItem:
    def _init_(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Order:
    def _init_(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def get_total(self):
        return sum(item.price for item in self.items)
        
    def clear(self):
        self.items = []

# ================= 2. Controllers =================
class OrderManager:
    def checkout(self, order):
        # هنا المفروض نربط بقاعدة البيانات لخصم المخزون وحفظ الفاتورة
        total = order.get_total()
        order.clear()
        return total

# ================= 3. GUI Views =================
class MenuFrame(ctk.CTkFrame):
    def _init_(self, master, menu_items, add_callback):
        super()._init_(master)
        self.grid_columnconfigure((0, 1), weight=1)
        
        title = ctk.CTkLabel(self, text="Menu - القائمة", font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=20)
        
        # إنشاء أزرار الأصناف ديناميكياً
        for index, item in enumerate(menu_items):
            row = (index // 2) + 1
            col = index % 2
            
            card = ctk.CTkFrame(self, fg_color="#2B2B2B", corner_radius=10)
            card.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
            
            ctk.CTkLabel(card, text=item.name, font=("Arial", 18, "bold")).pack(pady=(15,5))
            ctk.CTkLabel(card, text=f"{item.price} €", text_color="#10B981", font=("Arial", 16)).pack()
            
            btn = ctk.CTkButton(card, text="إضافة", fg_color="#F97316", hover_color="#EA580C",
                                command=lambda i=item: add_callback(i))
            btn.pack(pady=15, padx=20)

class CartFrame(ctk.CTkFrame):
    def _init_(self, master, checkout_callback):
        super()._init_(master, width=350)
        self.pack_propagate(False) # لمنع تغيير العرض تلقائياً
        
        ctk.CTkLabel(self, text="Current Order - الطلب الحالي", font=("Arial", 20, "bold")).pack(pady=20)
        
        # منطقة عرض الطلبات قابلة للتمرير
        self.items_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.items_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.total_label = ctk.CTkLabel(self, text="Total: 0.00 €", font=("Arial", 22, "bold"))
        self.total_label.pack(pady=15)
        
        self.checkout_btn = ctk.CTkButton(self, text="Checkout - دفع", fg_color="#2563EB", hover_color="#1D4ED8",
                                          height=40, font=("Arial", 16, "bold"), command=checkout_callback)
        self.checkout_btn.pack(pady=20, padx=20, fill="x")
        
    def update_cart(self, order):
        # مسح العناصر القديمة من السلة
        for widget in self.items_frame.winfo_children():
            widget.destroy()
            
        # إضافة العناصر الجديدة
        for item in order.items:
            item_lbl = ctk.CTkLabel(self.items_frame, text=f"• {item.name}    |    {item.price} €", font=("Arial", 14))
            item_lbl.pack(anchor="w", pady=5)
            
        self.total_label.configure(text=f"Total: {order.get_total():.2f} €")

# ================= 4. Main Application =================
class POSApp(ctk.CTk):
    def _init_(self):
        super()._init_()
        self.title("Food GUI Prototype")
        self.geometry("1000x650")
        ctk.set_appearance_mode("dark")
        
        # بيانات وهمية للتجربة (Mock Data)
        self.menu_items = [
            MenuItem(1, "Burger Menu", 12.50),
            MenuItem(2, "Pizza Margherita", 8.00),
            MenuItem(3, "Pasta Carbonara", 10.50),
            MenuItem(4, "Greek Salad", 6.00),
            MenuItem(5, "Iced Coffee", 4.50),
            MenuItem(6, "Cheesecake", 5.00),
        ]
        
        self.current_order = Order()
        self.order_manager = OrderManager()
        
        # ترتيب الشاشة
        self.cart_view = CartFrame(self, self.process_checkout)
        self.cart_view.pack(side="right", fill="y", padx=15, pady=15)
        
        self.menu_view = MenuFrame(self, self.menu_items, self.add_to_cart)
        self.menu_view.pack(side="left", fill="both", expand=True, padx=15, pady=15)

    def add_to_cart(self, item):
        self.current_order.add_item(item)
        self.cart_view.update_cart(self.current_order)
        
    def process_checkout(self):
        if not self.current_order.items:
            return
            
        total = self.order_manager.checkout(self.current_order)
        self.cart_view.update_cart(self.current_order) 
        
        # نافذة منبثقة بنجاح الدفع
        dialog = ctk.CTkToplevel(self)
        dialog.geometry("350x150")
        dialog.title("Success")
        dialog.attributes("-topmost", True) 
        ctk.CTkLabel(dialog, text=f"Order Completed!\nPaid: {total:.2f} €", font=("Arial", 18, "bold"), text_color="#10B981").pack(expand=True)

if _name_== "_main_":
    app = POSApp()
    app.mainloop()