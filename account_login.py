import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk



def login():
    try:
        username = retrieved_username.get()
        password = retrieved_password.get()

        confirmed_username = open('username.txt', 'r').read()
        confirmed_password = open('password.txt', 'r').read()

        if username == confirmed_username:

            if confirmed_password == password:
                login = 'Successful Login'
                successful.set(login)

            else:
                login = 'Incorrect Username or Password'
                successful.set(login)
        
        else:
            login = 'Incorrect Username or Password'
            successful.set(login)
    
    except UnboundLocalError:
        make_account = ttk.Label(master = root, text = 'No Account Has Been Registered to this IP.\n       Do You Need to Make an Account?', font = 'Calibri 15')
        make_account.pack()

        yes = ttk.Button(master = root, text = 'Yes')
        yes.pack(side = 'top')

    except FileNotFoundError:
        make_account = ttk.Label(master = root, text = 'No Account Has Been Registered to this IP.\n       Do You Need to Make an Account?', font = 'Calibri 15')
        make_account.pack()

        options = ttk.Frame(master = root)
        options.pack()

        yes = ttk.Button(master = options, text = 'Yes')
        yes.pack(side = 'left', padx = 1, pady = 10)

        no = ttk.Button(master = options, text = 'No')
        no.pack(side = 'left', padx = 10, pady = 10)


root = ttk.Window(themename = 'minty')
root.title('Account Login')
root.geometry('600x350')
root.resizable(width = False, height = False)

title=ttk.Label(master = root, text = 'Login', font = 'Calibri 21')
title.pack()

username_txt = ttk.Label(master = root, text = 'Username', font = 'Calibri 12')
username_txt.pack(pady = 0)

username = ttk.Frame(master = root)
retrieved_username = tk.StringVar()
username_entry = ttk.Entry(master = username, textvariable = retrieved_username, font = 'Calibri 10')
username.pack(pady = 0)
username_entry.pack(pady = 0)

password_txt = ttk.Label(master = root, text = 'Password', font = 'Calibri 12')
password_txt.pack(pady = 0)

password = ttk.Frame(master = root)
retrieved_password = tk.StringVar()
password_entry = ttk.Entry(master = password, textvariable = retrieved_password, font = 'Calibri 10')
password.pack(pady = 0)
password_entry.pack(pady = 0)

successful = tk.StringVar()
successful_label = ttk.Label(master = root, text = 'Output', font = 'Calibri 15', textvariable = successful)
successful_label.pack()

login = ttk.Button(master = password, text = 'Login', command = login)
login.pack(side = 'top', pady = 15)



root.mainloop()