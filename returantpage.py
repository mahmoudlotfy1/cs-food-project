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
        self.pp= False
    
 
        for m in self.name:
            self.b= i.CTkButton(self.scroll,fg_color="blue",text=m,width=200,command=  lambda k=m: self.press(k))
            self.b.pack(pady=9) 
    def press(self,k):
        v=self.name[k]

        if v != None :
            if self.pp ==False:
             self.pp= True
             self.scroll.pack_forget()
             v.pack(fill="both",expand=True)

        

        