import customtkinter as i
class scrollR:
    def __init__(self,master):
        self.master=master
       
        
        
        self.scroll= i.CTkScrollableFrame(self.master)
        self.scroll.pack(fill="both", expand= True)
class b(scrollR):
    def __init__(self, master,name):
        super().__init__(master)
        self.name=name
 
        for m in self.name:
            self.b= i.CTkButton(self.scroll,fg_color="blue",text=m,width=200)
            self.b.pack(pady=9) 
        

        