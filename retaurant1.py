import customtkinter as i
import json as j
from siginpage import siginpage
from loginpage import user as u
db="db.json"
uses="uses.json"
class Thefrontface:
    def __init__(self,master):
        self.master=master
        
        # --- 1. Memory Storage ---
        # This acts as our temporary database before we save to JSON
        self.current_restaurant_name = ""
        
        # --- 2. Restaurant Name Section ---
        self.name_label = i.CTkLabel(self.master, text="Restaurant Name:", font=("Arial", 16, "bold"))
        self.name_label.pack(pady=(20, 5))
        
        self.resturantname = i.CTkEntry(self.master, placeholder_text="Enter restaurant name", width=200)
        self.resturantname.pack(pady=5)
        
        self.approvename = i.CTkButton(self.master, text="Save Name", width=200, command= self.restaurantnamee)
        self.approvename.pack(pady=5)

        # --- Horizontal Line Separator ---
        i.CTkFrame(self.master, height=2, width=400, fg_color="gray").pack(pady=20)

        # --- 3. Add / Edit Food Section ---
        self.food_label = i.CTkLabel(self.master, text="Add or Edit Food:", font=("Arial", 16, "bold"))
        self.food_label.pack(pady=5)

        self.food_name_entry = i.CTkEntry(self.master, placeholder_text="Food Name (e.g. Burger)", width=200)
        self.food_name_entry.pack(pady=5)
        
        self.food_price_entry = i.CTkEntry(self.master, placeholder_text="Price (e.g. 15.99)", width=200)
        self.food_price_entry.pack(pady=5)

        self.add_food_btn = i.CTkButton(self.master, text="Save Food to Menu", width=200, command= self.adding)
        self.add_food_btn.pack(pady=10)
        
        # --- 4. The Scrollable Menu View ---
        self.menu_title = i.CTkLabel(self.master, text="Current Menu", font=("Arial", 16, "bold"))
        self.menu_title.pack(pady=(10, 0))
        
        self.scrollmenu = i.CTkScrollableFrame(self.master)
        self.scrollmenu.pack(pady=10, fill="both", expand=True, padx=20)

        # Load the menu for the first time
        

class thebackbone(Thefrontface):
    def __init__(self, master):
        super().__init__(master)
        self.x = ""
        self.n=False


    def restaurantnamee(self):
        ownername=self.resturantname.get()
        


        with open(uses,"r")as f:
            data= j.load(f)

        with open(db,"r")as f:
            dataa= j.load(f)   
        # just for safty we add it 
        if self.x not in data:
            data[self.x] = {"Resturant name": ""}

        
        self.rn = data[self.x]["Resturant name"]
        if self.rn !="":
            
            
            
            if self.rn!= ownername:
                data[self.x]["Resturant name"] = ownername
                with open(uses,"w")as f:
                  j.dump(data,f,indent=4)
                  # why do we need [] after restaurants? because it get all the list inside the resturant
                  # also we use forloop to find the dic inside the list bescause list is stupid that it
                for r in dataa.get("restaurants", []):
                    if r["name"] == self.rn:
                        r["name"] = ownername
                        break
                with open(db,"w")as f:
                 j.dump(dataa,f,indent=4)
                print("use and db done")

                
        if self.rn =="":
            print("your restaurant is named")
            data[self.x]["Resturant name"]=ownername
            with open(uses,"w")as f:
             j.dump(data,f,indent=4)
             #[] not "" to be able add stuff insde the list note ya lotfy
            new_restaurant = {"name": ownername,"dishes":[]}
            dataa["restaurants"].append(new_restaurant)
            with open(db,"w")as f:
                j.dump(dataa,f,indent=4)
            print("both are added")

        self.rn = ownername
        # refresh it everytime
        self.refresh()
    
    def adding(self):
        

        ownername=self.resturantname.get()

        food_name=self.food_name_entry.get()
        food_price=self.food_price_entry.get()
        if food_name and food_price:
         with open(db,"r")as f:
            dataa= j.load(f)    
        
         for restaurant in dataa.get("restaurants", []):
          if restaurant["name"] == ownername:
             restaurant["dishes"].append({"name": food_name, "price": float(food_price)})
             # inside the dishes there is empty list
             # we use break so python don't try oversmart me
        
             break
         with open(db, "w") as f:
                j.dump(dataa, f, indent=4)
         self.food_name_entry.delete(0, 'end')
         self.food_price_entry.delete(0, 'end')
         # w to rewrite everything
         print("food is saved")

         self.refresh()
        
       

       

        
            
    def removing(self, food_r):
        
           with open(db,"r")as f:
            dataa= j.load(f)
            for o in dataa.get("restaurants",[]):
                if o["name"]==self.rn:
                    update_dishes=[]
                    for aa in o.get("dishes",[]):
                        #it create now list the remove the part we want to remove. sorry little dishes :(.
                        if aa["name"]!=food_r["name"]:
                            update_dishes.append(aa)
                    o["dishes"]= update_dishes

            with open(db, "w") as f:
                j.dump(dataa, f, indent=4)

            self.refresh()
           
       

           
           
    def changingprice(self,nnp):
        # we inserd
        
        e=self.food_price_entry.get()
        with open(db,"r")as f:
            dataa= j.load(f)
            for o in dataa.get("restaurants",[]):
                if o["name"]==self.rn:
                    
                    for aa in o.get("dishes",[]):
                        if aa["name"]==nnp["name"]:
                            if e !="":

                              aa["price"]=e
                            else:
                                print("pls enter num")
                    
            

                            
                    
           # clean up job
            with open(db, "w") as f:
                j.dump(dataa, f, indent=4)
                # food_name is kinda meh but it's still safe to have it
            self.food_name_entry.delete(0,"end")
            self.food_price_entry.delete(0,"end")

            self.refresh()
           
        
        
        
        

    def refresh(self):
       # to stop it from duplicating every scroll have an id which can't be uses twice that is the winfo
       # where widget destroy the old scroll and keep the new one because scroll save all of them and adding more will put old with new
       for widget in self.scrollmenu.winfo_children():
        widget.destroy()
       with open(db,"r")as f:
            dataa= j.load(f)

       xx = []
           
       for q in dataa.get("restaurants",[]):
           if q["name"]==self.rn:
               xx=q.get("dishes",[])
       for x in xx:
           name = x["name"]
           price = x["price"]
           row= i.CTkFrame(self.scrollmenu, fg_color="transparent")
           row.pack(fill="x", pady=2)
           i.CTkButton(row, text=f"{name} Price {price}$", command=lambda showing=x: print(showing)).pack(side="left",fill="x", expand=True,padx=5,pady=3)
           i.CTkButton(row, text="trash", fg_color="red",hover_color="darkred", command=lambda food=x: self.removing(food) ).pack(side="right", padx=5,pady=3)
           i.CTkButton(row, text="change price", command=lambda p=x: self.changingprice(p) ).pack(side="right",padx=5,pady=3)
           
        
    
            


    
    
    

