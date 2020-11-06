import tkinter as app
from tkinter import messagebox
from tkinter import Scrollbar
import random

#definitions
family = "sans serif"
primary_c = "#2065d4"
second_c = "#e8e8e8"
inherit = "white"
algorithm_count = 5
keywords = []
passwords = []

window = app.Tk()
window.title("Password Generator")
window.config(bg=inherit)

#elements

scrollbar = Scrollbar(window)
scrollbar.pack( side = app.RIGHT, fill = app.Y )

main_header = app.Label(window, text="PASSWORD GENERATOR",fg=primary_c, bg=inherit, font=(family, 24), pady=10, padx=20)

sub_info = app.Label(window, text="This program generates passwords using the keywords you enter. Currently, the program is using {} algorithm(s) to generate passwords.".format(algorithm_count), fg="grey", bg=inherit, font=(family, 12), wraplength=440, justify=app.LEFT, pady=10, padx=10)

input_box = app.Entry(window,font=(family, 16), width=30, borderwidth=10, fg=primary_c, bg=second_c, relief=app.FLAT)

submit = app.Button(window, text="Generate", font=(family, 12), width=35, borderwidth=5,relief=app.RAISED, bg=primary_c,activebackground=primary_c, fg=inherit, activeforeground=inherit)

pass_header = app.Label(window, text="Passwords", fg=primary_c, bg=inherit, pady=10, font=(family, 16))

pass_list = app.Listbox(window, yscrollcommand = scrollbar.set, bg=primary_c, fg=inherit, font=(family, 12), width=42, bd=5)


def main():
    
    submit.config(command = start_app)

    #packing
    main_header.pack()
    sub_info.pack()
    input_box.pack()
    add_space(window, 1)
    submit.pack()
    pass_header.pack()
    pass_list.pack()
    add_space(window, 1)

    scrollbar.config( command = pass_list.yview )
    window.mainloop()


#functions
def add_space(master, amount):
    white_space = app.Label(master, text=" ", height=amount, bg=inherit)
    white_space.pack()

def start_app():

    input = input_box.get()
    if not input:
        messagebox.showwarning("No Input", "Enter some keywards first")
        return 1

    keywords = input.split()
    pass_list.delete(0, app.END)

    #generating passwords
    algo_1(keywords, pass_list)
    algo_2(keywords, pass_list)
    algo_3(keywords, pass_list)
    algo_4(keywords, pass_list)
    algo_5(keywords, pass_list)
    

#algorithms    
def algo_1(words, list):

    password = str(random.randint(0,9))*random.randint(0, 5) + str("".join(words)) + str(random.randint(0,9))*random.randint(0, 5)

    list.insert(app.END, password)
    
def algo_2(words, list):

    password = ""

    for word in words:
        for char in word:
            if random.randint(0, 1):
                password += char.upper()
            else:
                password += char.lower()
                
    list.insert(app.END, password)

def algo_3(words, list):

    password = ""

    for word in words:
        if random.randint(0, 1):
            password += word.upper()
        else:
            password += word.lower()

        password += str(random.randint(0,9))*random.randint(1, 5)
                
    list.insert(app.END, password)

def algo_4(words, list):

    password = ""

    password += str(chr(random.randint(33,47)))*random.randint(1, 5)

    for word in words:
        if random.randint(0, 1):
            password += word.capitalize()
        else:
            password += word.lower()

    password += str(chr(random.randint(33,47)))*random.randint(1, 5)
                
    list.insert(app.END, password)

def algo_5(words, list):

    password = ""

    password += str(chr(random.randint(33,47)))*random.randint(1, 5)

    for word in words:
        if random.randint(0, 1):
            password += word.capitalize()
        else:
            password += word.lower()
        password += str(random.randint(0,9))*random.randint(1, 5)
                
    list.insert(app.END, password)
    

main()
