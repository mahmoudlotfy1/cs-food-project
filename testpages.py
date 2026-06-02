"""""
import customtkinter as i
import ownerpage
rt=i.CTk()
i.set_appearance_mode("light")
i.set_default_color_theme("blue")
rt.geometry('700x700')

ooo= i.CTkFrame(rt)
# pass by refrence we use qqq to show ooo belonge to ownerpage
ownerpage.owner(ooo)

rt.mainloop()
"""