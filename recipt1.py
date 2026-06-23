import customtkinter as ctk
import datetime
import random

class The_truck(ctk.CTkFrame):
    def __init__(self,controll,order_items, order_total):
        #why is should be controll the use root and why we us root
        super().__init__(controll.root)
        self.controll= controll
        self.order_items=order_items
        self.order_total=order_total
        minutes_to_wait = random.randint(20, 45)
        arrival_time = (datetime.datetime.now() + datetime.timedelta(minutes=minutes_to_wait)).strftime("%I:%M %p")
        car_text=ctk.CTkLabel(self, text="🚚 Order Confirmed!", font=("Arial", 20, "bold"), text_color="green")
        car_text.pack(pady=5)
        ar=ctk.CTkLabel(self, text=f"Estimated Arrival: {arrival_time}", font=("Arial", 16))
        ar.pack(pady=5)


class main_rc(The_truck):
    def __init__(self, controll, order_items, order_total):
        super().__init__(controll, order_items, order_total)

        self.yr= ctk.CTkLabel(self, text="Your Receipt", font=("Arial", 24, "bold"))
        self.yr.pack(pady=20)

        self.details_frame = ctk.CTkScrollableFrame(self, height=200)
        self.details_frame.pack(fill="both", expand=True, padx=20, pady=10)
        # why in label we use detail_frame master not self only?
        self.d_f=ctk.CTkLabel(self.details_frame, text="Order Summary:", font=("Arial", 16, "bold"))
        self.d_f.pack(anchor="w", pady=5)

        for item in self.order_items:
            text = f"{item['name']} ({item['from']})  ........  ${item['price']}"
            ctk.CTkLabel(self.details_frame, text=text).pack(anchor="w", pady=2)
            #x is horizontal
        ctk.CTkFrame(self, height=2, fg_color="gray").pack(fill="x", padx=40, pady=10) # Horizontal line
        ctk.CTkLabel(self, text=f"Total Paid: ${self.order_total:.2f}", font=("Arial", 20, "bold")).pack(pady=5)
        hm=ctk.CTkButton(self, text="Back to Home", command=self.go_home)
        hm.pack(pady=20)
    def go_home(self):
        # Send the user back to the main restaurant list
        self.controll.show_home()

        