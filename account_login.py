import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
    

# create login function
def create_account():
    try:
        username_list_create = open('username.txt', 'x')

        try:
            username_list = open('username.txt', 'a')

            username = retrieved_username.get()
            password = retrieved_password.get()
            confirm_password = retrieved_confirm_password.get()

            username_list_txt = open('username.txt', 'r')
            username_list_read = username_list_txt.read()
            username_list_txt.close()

            if username == username_list_read:

                print('Username not available')
            
            else:
                username_list.write(username)
                username_list.close()
                if password == confirm_password:
                    created_account = 'You have successfully created your account!'
                else:
                    created_account = 'Passwords do not match!'

            successful.set(created_account)

        except UnboundLocalError:
            already_account_label = ttk.Label(master = root, text = 'An account is already registered with this IP. Try logging in', font = 'Calibri 15') 
            already_account_label.pack()

    except UnboundLocalError:
       already_account_label = ttk.Label(master = root, text = 'An account is already registered with this IP. Try logging in', font = 'Calibri 15') 
       already_account_label.pack()

    except FileExistsError:
        already_account_label = ttk.Label(master = root, text = 'An account is already registered with this IP. Try logging in', font = 'Calibri 15') 
        already_account_label.pack()
    
    
# create window
root = ttk.Window(themename = 'minty')
root.title('Account Creation')
root.geometry('600x350')
root.resizable(width = False, height = False)

# create widgits
title = ttk.Label(master = root, text = 'Create Account', font = 'Calibri 21 bold')
title.pack(pady = 5)

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

confirm_password_text = ttk.Label(master = root, text = 'Confirm Password', font = 'Calibri 12')
confirm_password_text.pack(pady = 0)

confirm_password = ttk.Frame(master = root)
retrieved_confirm_password = tk.StringVar()
confrim_password_entry = ttk.Entry(master = confirm_password, textvariable = retrieved_confirm_password, font = 'Calibri 10')
confirm_password.pack(pady = 0)
confrim_password_entry.pack(pady = 0)

login = ttk.Button(master = confirm_password, text = 'Create Account', command = create_account)
login.pack(side = 'top', pady = 25)

successful = tk.StringVar()
successful_label = ttk.Label(master = root, text = 'Output', font = 'Calibri 15', textvariable = successful)
successful_label.pack()

root.mainloop()
