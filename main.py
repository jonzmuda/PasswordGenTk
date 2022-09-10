import tkinter
import customtkinter
from tkinter import *
import random
import string

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root_tk = customtkinter.CTk()  
root_tk.geometry("400x240")
root_tk.resizable(False,False)
root_tk.title("Random Password Generator")
password = []
def exit_program():
    print("Exiting Program")
    root_tk.destroy()
def generate_password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    length = int(s2.get())
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    print("Your random password is", "".join(password))
    generated_password = "".join(password)
    l = Label(root_tk, text = f"{generated_password}")
    customtkinter.CTkTextbox(font =("Courier", 14), bg='white')
    l.place(relx=0.5, rely=0.50, anchor=S)


exit_button = customtkinter.CTkButton(master=root_tk, command=exit_program, text="Exit")
exit_button.place(relx=0.5, rely=0.95, anchor=tkinter.S)

generate_button = customtkinter.CTkButton(master=root_tk, command=generate_password, text="Generate")
generate_button.place(relx=0.5, rely=0.80, anchor=tkinter.S)

v2 = DoubleVar()
  
def show2():
      
    str(v2.get()) 
  
s2 = customtkinter.CTkSlider(master=root_tk, from_=5, to=15, number_of_steps=10)
slider_length = s2.get()
  
s2.place(relx =0.5, rely=0.65, anchor = S) 


root_tk.iconbitmap('C:\\Users\\jonzm\\OneDrive\\Desktop\\Projects\\Coding\\Tkninter\\ic_vpn_lock_128_28770.ico')
root_tk.mainloop()

