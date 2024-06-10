from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import pandas as pd
from tkinter import filedialog
import csv

#landing page
class LandingPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Landing Page")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        # Create a frame to hold the background image with a black border
        bg_frame = Frame(self.root, bg="black", bd=4)
        bg_frame.place(x=280, y=140)

        # Load the background image and resize it
        self.bg_image = PhotoImage(file="background_image.png")  # Replace "background_image.png" with your image file

        # Create a label to display the background image
        bg_label = Label(bg_frame, image=self.bg_image)
        bg_label.pack(fill="both", expand=True)

        heading_label = Label(self.root, text="Student Database System", font=("Arial", 24, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(50, 20))  # Adjusted padding for top and bottom

        # Create a frame for button layout
        button_frame = Frame(self.root, bg="#f0f0f0")
        button_frame.pack(expand=True, pady=(150, 0))  # Add padding only to the top

        # Define button styles
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",  # Set the button border color to black
            "highlightthickness": 4,  # Set the border thickness
            "width": 10,  # Set a fixed width for the buttons
        }

        self.btn_login = Button(button_frame, text="Login", command=self.open_login_window, **btn_style)
        self.btn_login.pack(pady=10, ipady=5, side=LEFT, padx=5)  # Removed ipadx

        self.btn_register = Button(button_frame, text="Register", command=self.open_register_window, **btn_style)
        self.btn_register.pack(pady=10, ipady=5, side=LEFT, padx=5)  # Removed ipadx

        # Create a label for the statement
        statement_label = Label(self.root, text="Made by : Anshul Patil, VNIT", font=("Arial", 12), bg="#f0f0f0")
        # Place the label slightly above the bottom center of the window
        statement_label.place(relx=0.5, rely=.90, anchor="s")

        guide_label = Label(self.root, text="Guided by : Nidhi Pandey", font=("Arial", 12), bg="#f0f0f0")
        # Place the label slightly above the bottom center of the window
        guide_label.place(relx=0.5, rely=0.93, anchor="s")


    def open_login_window(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginPage(login_window)

    def open_register_window(self):
        self.root.destroy()
        register_window = Tk()
        register_app = RegisterPage(register_window)




#-----------------------------------------------------------------------------------------------------------------------


#loginpage
class LoginPage:
        def __init__(self, root):
            self.root = root
            self.root.title("Login Page")
            self.root.geometry("790x700+300+0")
            self.root.config(bg="#f0f0f0")  # Set background color

            # Heading Label
            heading_label = Label(self.root, text="Login Page", font=("Arial", 20, "bold"), bg="#f0f0f0")
            heading_label.pack(pady=(50, 20))

            # Button Frame
            button_frame = Frame(self.root, bg="#f0f0f0")
            button_frame.pack(expand=True, pady=10)

            # Button Style
            btn_style = {
                "bg": "#4DA8FF",
                "fg": "white",
                "font": ("Arial", 14),
                "padx": 20,
                "pady": 10,
                "highlightbackground": "black",
                "highlightthickness": 2,
                "width": 15,
            }

            btn_style_back = {
                "bg": "red",
                "fg": "white",
                "font": ("Arial", 14),
                "padx": 20,
                "pady": 10,
                "highlightbackground": "black",
                "highlightthickness": 2,
                "width": 15,
            }

            # Login Buttons
            self.btn_instructor = Button(button_frame, text="Login as Instructor", command=self.login_instructor,
                                         **btn_style)
            self.btn_instructor.pack(pady=10)

            self.btn_student = Button(button_frame, text="Login as Student", command=self.login_student, **btn_style)
            self.btn_student.pack(pady=10)

            self.btn_admin = Button(button_frame, text="Login as Admin", command=self.login_admin, **btn_style)
            self.btn_admin.pack(pady=10)

            self.btn_admin = Button(button_frame, text="Back", command=self.back, **btn_style_back)
            self.btn_admin.pack(pady=10)

        def login_instructor(self):
            self.root.destroy()
            login_window = Tk()
            login_app = LoginWindowInstructor(login_window)

        def login_student(self):
            self.root.destroy()
            login_window = Tk()
            login_app = LoginWindowStudent(login_window)

        def login_admin(self):
            self.root.destroy()
            login_window = Tk()
            login_app = LoginWindowAdmin(login_window)

        def back(self):
            self.root.destroy()
            login_window = Tk()
            login_app = LandingPage(login_window)



#-----------------------------------------------------------------------------------------------------------------------


#resgisterpage
class RegisterPage:

    def __init__(self, root):
        self.root = root
        self.root.title("Register Page")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        # Heading Label
        heading_label = Label(self.root, text="Register Page", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(50, 20))

        # Button Frame
        button_frame = Frame(self.root, bg="#f0f0f0")
        button_frame.pack(expand=True, pady=10)

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Register Buttons
        self.btn_instructor = Button(button_frame, text="Register as Instructor", command=self.register_instructor,
                                      **btn_style)
        self.btn_instructor.pack(pady=10)

        self.btn_student = Button(button_frame, text="Register as Student", command=self.register_student, **btn_style)
        self.btn_student.pack(pady=10)

        self.btn_admin = Button(button_frame, text="Register as Admin", command=self.register_admin, **btn_style)
        self.btn_admin.pack(pady=10)

        self.btn_admin = Button(button_frame, text="Back", command=self.back, **btn_style_back)
        self.btn_admin.pack(pady=10)

    def register_instructor(self):
        # Add code for instructor registration RegisterWindowInstructor
        self.root.destroy()
        login_window = Tk()
        login_app = RegisterWindowInstructor(login_window)

    def register_student(self):
        # Add code for student registration
        self.root.destroy()
        login_window = Tk()
        login_app = RegisterWindowStudent(login_window)

    def register_admin(self):
        # Add code for admin registration
        self.root.destroy()
        login_window = Tk()
        login_app = RegisterWindowAdmin(login_window)

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LandingPage(login_window)





#-----------------------------------------------------------------------------------------------------------------------



#logininstructor
class LoginWindowInstructor:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Login as Instructor", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the form
        form_frame = Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        # Username label and entry
        self.lbl_username = Label(form_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = Entry(form_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.lbl_password = Label(form_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(form_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Login button
        self.btn_login = Button(self.root, text="Login", command=self.login, **btn_style)
        self.btn_login.pack(pady=(60, 10))  # Increased top padding to move the button above

        # Back button
        self.btn_back = Button(self.root, text="Back", command=self.back, **btn_style_back)
        self.btn_back.pack(pady=(0, 20))  # Decreased bottom padding to make the button lower

    def login(self):
        # Get the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate if username and password are not empty
        if username.strip() == '' or password.strip() == '':
            tkinter.messagebox.showerror("Login Error", "Please enter both username and password.")
            return

        # Connect to the database and check if the user exists
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()
            # Execute an SQL query to retrieve the user with the given username and password
            cur.execute("SELECT instructor_id,instructor_password FROM users WHERE instructor_id=%s AND instructor_password=%s", (username, password))
            user = cur.fetchone()
            if user:
                self.root.destroy()  # Close login window
                open_main_app(username)  # Open main application and pass username
            else:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Login Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginPage(login_window)

#loginstudent
class LoginWindowStudent:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Login as Student", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the form
        form_frame = Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        # Username label and entry
        self.lbl_username = Label(form_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = Entry(form_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.lbl_password = Label(form_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(form_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Login button
        self.btn_login = Button(self.root, text="Login", command=self.login, **btn_style)
        self.btn_login.pack(pady=(60, 10))  # Increased top padding to move the button above

        # Back button
        self.btn_back = Button(self.root, text="Back", command=self.back, **btn_style_back)
        self.btn_back.pack(pady=(0, 20))  # Decreased bottom padding to make the button lower

        global_username = self.entry_username.get()

    def login(self):
        # Get the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate if username and password are not empty
        if username.strip() == '' or password.strip() == '':
            tkinter.messagebox.showerror("Login Error", "Please enter both username and password.")
            return

        # Connect to the database and check if the user exists
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()
            # Execute an SQL query to retrieve the user with the given username and password
            cur.execute("SELECT student_id,student_password FROM users WHERE student_id=%s AND student_password=%s", (username, password))
            user = cur.fetchone()
            if user:
                self.root.destroy()  # Close login window
                open_main_app_student(username)  # Open main application
            else:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Login Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginPage(login_window)

#loginadmin
class LoginWindowAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Login as Admin", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the form
        form_frame = Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        # Username label and entry
        self.lbl_username = Label(form_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = Entry(form_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.lbl_password = Label(form_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(form_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.btn_login = Button(self.root, text="Login", command=self.login, **btn_style)
        self.btn_login.pack(pady=(60, 10))  # Increased top padding to move the button above

        # Back button
        self.btn_back = Button(self.root, text="Back", command=self.back, **btn_style_back)
        self.btn_back.pack(pady=(0, 20))  # Decreased bottom padding to make the button lower

    def login(self):
        # Get the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate if username and password are not empty
        if username.strip() == '' or password.strip() == '':
            tkinter.messagebox.showerror("Login Error", "Please enter both username and password.")
            return

        # Connect to the database and check if the user exists
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()
            # Execute an SQL query to retrieve the user with the given username and password
            cur.execute("SELECT admin_id,admin_password FROM users WHERE admin_id=%s AND admin_password=%s", (username, password))
            user = cur.fetchone()
            if user:
                self.root.destroy()  # Close login window
                open_main_app_admin(username)  # Open main application
            else:
                tkinter.messagebox.showerror("Login Error", "Invalid username or password.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Login Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginPage(login_window)




#-----------------------------------------------------------------------------------------------------------------------





#registerinstructor
class RegisterWindowInstructor:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Register as Instructor", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the form
        form_frame = Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        # Username label and entry
        self.lbl_username = Label(form_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = Entry(form_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.lbl_password = Label(form_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(form_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Register button
        self.btn_register = Button(self.root, text="Register", command=self.register, **btn_style)
        self.btn_register.pack(pady=(60, 10))  # Increased top padding to move the button above

        # Back button
        self.btn_back = Button(self.root, text="Back", command=self.back, **btn_style_back)
        self.btn_back.pack(pady=(0, 20))  # Decreased bottom padding to make the button lower

    def register(self):
        # Get the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate if username and password are not empty
        if username.strip() == '' or password.strip() == '':
            tkinter.messagebox.showerror("Registration Error", "Please enter both username and password.")
            return

        # Validate if the username starts with "INS"
        if not username.startswith("INS"):
            tkinter.messagebox.showerror("Registration Error", "Username should start with 'INS'.")
            return

        # Connect to the database and insert the new user record
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()
            # Insert the new user into your users table, assuming you have a table named 'users'
            cur.execute("INSERT INTO users (instructor_id, instructor_password) VALUES (%s, %s)", (username, password))
            sqlCon.commit()
            tkinter.messagebox.showinfo("Registration Success", "User registered successfully.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Registration Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = RegisterPage(login_window)


#resgisterstudent
class RegisterWindowStudent:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Register as Student", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the form
        form_frame = Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        # Username label and entry
        self.lbl_username = Label(form_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = Entry(form_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.lbl_password = Label(form_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(form_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Login button
        self.btn_login = Button(self.root, text="Register", command=self.register, **btn_style)
        self.btn_login.pack(pady=(60, 10))  # Increased top padding to move the button above

        # Back button
        self.btn_back = Button(self.root, text="Back", command=self.back, **btn_style_back)
        self.btn_back.pack(pady=(0, 20))  # Decreased bottom padding to make the button lower

    def register(self):
        # Get the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate if username and password are not empty
        if username.strip() == '' or password.strip() == '':
            tkinter.messagebox.showerror("Registration Error", "Please enter both username and password.")
            return

        # Validate if the username is a 5-digit number
        if not (username.isdigit() and len(username) == 5):
            tkinter.messagebox.showerror("Registration Error", "Username must be a 5-digit number.")
            return

        # Connect to the database and insert the new user record
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()
            # Insert the new user into your users table, assuming you have a table named 'users'
            cur.execute("INSERT INTO users (student_id, student_password) VALUES (%s, %s)", (username, password))
            sqlCon.commit()
            tkinter.messagebox.showinfo("Registration Success", "User registered successfully.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Registration Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()
    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = RegisterPage(login_window)


#registeradmin
class RegisterWindowAdmin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Register as Admin", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the form
        form_frame = Frame(self.root, bg="#f0f0f0")
        form_frame.pack(pady=20)

        # Username label and entry
        self.lbl_username = Label(form_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = Entry(form_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        # Password label and entry
        self.lbl_password = Label(form_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        self.lbl_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = Entry(form_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        # Login button
        self.btn_login = Button(self.root, text="Register", command=self.register, **btn_style)
        self.btn_login.pack(pady=(60, 10))  # Increased top padding to move the button above

        # Back button
        self.btn_back = Button(self.root, text="Back", command=self.back, **btn_style_back)
        self.btn_back.pack(pady=(0, 20))  # Decreased bottom padding to make the button lower

    def register(self):
        # Get the username and password entered by the user
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Validate if username and password are not empty
        if username.strip() == '' or password.strip() == '':
            tkinter.messagebox.showerror("Registration Error", "Please enter both username and password.")
            return


        # Validate if the username starts with "ADN"
        if not username.startswith("ADN"):
            tkinter.messagebox.showerror("Registration Error", "Username should start with 'ADN'.")
            return


        # Connect to the database and insert the new user record
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()
            # Insert the new user into your users table, assuming you have a table named 'users'
            cur.execute("INSERT INTO users (admin_id, admin_password) VALUES (%s, %s)", (username, password))
            sqlCon.commit()
            tkinter.messagebox.showinfo("Registration Success", "User registered successfully.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Registration Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = RegisterPage(login_window)




#-----------------------------------------------------------------------------------------------------------------------




class MainPageinstructor:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Main Page")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Main Page", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Display username
        username_label = Label(self.root, text=f"Welcome, {self.username}", font=("Arial", 16), bg="#f0f0f0")
        username_label.pack(pady=(10, 20))

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the buttons
        button_frame = Frame(self.root, bg="#f0f0f0")
        button_frame.pack()

        # Student Details button
        self.btn_student_details = Button(button_frame, text="Student Details", command=self.open_student_details, **btn_style)
        self.btn_student_details.grid(row=0, column=0, padx=10, pady=10)

        # Student Subject Details button
        self.btn_student_subject_details = Button(button_frame, text="Student Subject Details", command=self.open_student_subject_details, **btn_style)
        self.btn_student_subject_details.grid(row=0, column=1, padx=10, pady=10)

        # Student Project Details button
        self.btn_student_project_details = Button(button_frame, text="Student Project Details", command=self.open_student_project_details, **btn_style)
        self.btn_student_project_details.grid(row=1, column=0, padx=10, pady=10)

        # Student Activity Details button
        self.btn_student_activity_details = Button(button_frame, text="Student Activity Details", command=self.open_student_activity_details, **btn_style)
        self.btn_student_activity_details.grid(row=1, column=1, padx=10, pady=10)

        self.btn_student_faculty_details = Button(button_frame, text="Student Faculty Details", command=self.open_student_faculty_details, **btn_style)
        self.btn_student_faculty_details.grid(row=2, column=0, padx=10, pady=10)

        self.btn_student_faculty_details = Button(button_frame, text="Log-Out", command=self.back, **btn_style_back)
        self.btn_student_faculty_details.grid(row=2, column=1, padx=10, pady=10)

    def open_student_details(self):
        # Function to handle opening the Student Details page
        username = self.username  # Retrieve the username from the instance variable
        self.root.destroy()
        student_window = Tk()
        student_app = Student_details(student_window, username)  # Pass the username to the Student_details class

    def open_student_subject_details(self):
        # Function to handle opening the Student Subject Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = student_subject_details(login_window, username)

    def open_student_project_details(self):
        # Function to handle opening the Student Project Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = student_project_details(login_window, username)

    def open_student_activity_details(self):
        # Function to handle opening the Student Activity Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = student_activity_details(login_window, username)

    def open_student_faculty_details(self):
        # Function to handle opening the Student Activity Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = student_faculty_details(login_window, username)

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginWindowInstructor(login_window)


def open_main_app(username):
    root = Tk()
    application = MainPageinstructor(root, username)
    root.mainloop()


class MainPageadmin:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Main Page")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Main Page", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down

        # Display username
        username_label = Label(self.root, text=f"Welcome, {self.username}", font=("Arial", 16), bg="#f0f0f0")
        username_label.pack(pady=(10, 20))

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the buttons
        button_frame = Frame(self.root, bg="#f0f0f0")
        button_frame.pack()

        # Student Details button
        self.btn_student_details = Button(button_frame, text="Student Details", command=self.open_student_details, **btn_style)
        self.btn_student_details.grid(row=0, column=0, padx=10, pady=10)

        # Student Subject Details button
        self.btn_student_subject_details = Button(button_frame, text="Student Subject Details", command=self.open_student_subject_details, **btn_style)
        self.btn_student_subject_details.grid(row=0, column=1, padx=10, pady=10)

        # Student Project Details button
        self.btn_student_project_details = Button(button_frame, text="Student Project Details", command=self.open_student_project_details, **btn_style)
        self.btn_student_project_details.grid(row=1, column=0, padx=10, pady=10)

        # Student Activity Details button
        self.btn_student_activity_details = Button(button_frame, text="Student Activity Details", command=self.open_student_activity_details, **btn_style)
        self.btn_student_activity_details.grid(row=1, column=1, padx=10, pady=10)

        self.btn_student_faculty_details = Button(button_frame, text="Student Faculty Details", command=self.open_student_faculty_details, **btn_style)
        self.btn_student_faculty_details.grid(row=2, column=0, padx=10, pady=10)

        self.btn_student_faculty_details = Button(button_frame, text="Log-Out",
                                                  command=self.back, **btn_style_back)
        self.btn_student_faculty_details.grid(row=2, column=1, padx=10, pady=10)

    def open_student_details(self):
        # Function to handle opening the Student Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = Student_basicDetailsWindowadminview(login_window,username)

    def open_student_subject_details(self):
        # Function to handle opening the Student Subject Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = Student_semesterDetailsWindowadminview(login_window,username)

    def open_student_project_details(self):
        # Function to handle opening the Student Project Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = Student_projectDetailsWindowadminview(login_window,username)

    def open_student_activity_details(self):
        # Function to handle opening the Student Activity Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = Student_activityDetailsWindowadminview(login_window,username)

    def open_student_faculty_details(self):
        # Function to handle opening the Student Activity Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = Student_subjectDetailsWindowadminview(login_window,username)

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginWindowAdmin(login_window)

def open_main_app_admin(username):
    root = Tk()
    application = MainPageadmin(root, username)
    root.mainloop()


class MainPagestudent:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Main Page")
        self.root.geometry("790x700+300+0")
        self.root.config(bg="#f0f0f0")  # Set background color

        heading_label = Label(self.root, text="Main Page", font=("Arial", 20, "bold"), bg="#f0f0f0")
        heading_label.pack(pady=(70, 60))  # Adjusted padding to shift the heading down
        username_label = Label(self.root, text=f"Welcome, {self.username}", font=("Arial", 16), bg="#f0f0f0")
        username_label.pack(pady=(10, 20))

        # Button Style
        btn_style = {
            "bg": "#4DA8FF",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        btn_style_back = {
            "bg": "red",
            "fg": "white",
            "font": ("Arial", 14),
            "padx": 20,
            "pady": 10,
            "highlightbackground": "black",
            "highlightthickness": 2,
            "width": 15,
        }

        # Create a frame for the buttons
        button_frame = Frame(self.root, bg="#f0f0f0")
        button_frame.pack()

        # Student Details button
        self.btn_student_details = Button(button_frame, text="Student Details", command=self.open_student_details, **btn_style)
        self.btn_student_details.grid(row=0, column=0, padx=10, pady=10)

        # Student Subject Details button
        self.btn_student_subject_details = Button(button_frame, text="Student Subject Details", command=self.open_student_subject_details, **btn_style)
        self.btn_student_subject_details.grid(row=0, column=1, padx=10, pady=10)

        # Student Project Details button
        self.btn_student_project_details = Button(button_frame, text="Student Project Details", command=self.open_student_project_details, **btn_style)
        self.btn_student_project_details.grid(row=1, column=0, padx=10, pady=10)

        # Student Activity Details button
        self.btn_student_activity_details = Button(button_frame, text="Student Activity Details", command=self.open_student_activity_details, **btn_style)
        self.btn_student_activity_details.grid(row=1, column=1, padx=10, pady=10)

        self.btn_student_faculty_details = Button(button_frame, text="Student Faculty Details", command=self.open_student_faculty_details, **btn_style)
        self.btn_student_faculty_details.grid(row=2, column=0, padx=10, pady=10)

        self.btn_student_faculty_details = Button(button_frame, text="Log-Out",
                                                  command=self.back, **btn_style_back)
        self.btn_student_faculty_details.grid(row=2, column=1, padx=10, pady=10)

    def open_student_details(self):
        # Function to handle opening the Student Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = StudentDetailsDisplayWindow(login_window,username)

    def open_student_subject_details(self):
        # Function to handle opening the Student Subject Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = SemesterDetailsDisplayWindow(login_window,username)

    def open_student_project_details(self):
        # Function to handle opening the Student Project Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = ProjectDetailsDisplayWindow(login_window,username)

    def open_student_activity_details(self):
        # Function to handle opening the Student Activity Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = StudentActivityDisplayWindow(login_window,username)

    def open_student_faculty_details(self):
        # Function to handle opening the Student Activity Details page
        username = self.username
        self.root.destroy()
        login_window = Tk()
        login_app = FacultyDetailsDisplayWindow(login_window,username)



    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = LoginWindowStudent(login_window)


def open_main_app_student(username):
    root = Tk()
    application = MainPagestudent(root,username)
    root.mainloop()




#-----------------------------------------------------------------------------------------------------------------------




#instructor functions
class Student_details:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Update title to include username  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2, relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        StudentID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
        YearofStudy = StringVar()
        DOB = StringVar()
        email = StringVar()
        roll = StringVar()

        # ----------------------------------------------------------------------------------------------------

        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageinstructor(login_window, self.username)  # Pass the username to MainPageinstructor

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields
            StudentID.set("")
            Firstname.set("")
            Surname.set("")
            YearofStudy.set("")
            DOB.set("")
            roll.set("")
            Mobile.set("")
            Address.set("")
            Gender.set("")
            email.set("")

            # Clear data displayed in the Treeview widget
            self.student_records.delete(*self.student_records.get_children())

            # Clear variables associated with display fields
            StudentID.set("")
            Firstname.set("")
            Surname.set("")
            YearofStudy.set("")
            DOB.set("")
            roll.set("")
            Mobile.set("")
            Address.set("")
            Gender.set("")
            email.set("")

        def exportData():
            try:
                # Open a file dialog to select the export file
                file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

                if file_path:
                    # Open the file in write mode
                    with open(file_path, 'w', newline='') as file:
                        writer = csv.writer(file)
                        # Write column headers
                        writer.writerow(["Student ID", "Firstname", "Surname", "Year of Study", "DOB", "Roll Number",
                                         "Mobile", "Address", "Gender", "Email"])

                        # Iterate over the records in the Treeview widget and write them to the CSV file
                        for row_id in self.student_records.get_children():
                            row = self.student_records.item(row_id)['values']
                            writer.writerow(row)

                    tkinter.messagebox.showinfo("Export Data", "Data exported successfully.")
            except Exception as e:
                tkinter.messagebox.showerror("Export Data", f"An error occurred: {e}")

        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "" or Mobile.get() == "" or YearofStudy.get() == "" or DOB.get() == "" or email.get() == "" :
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Check if Student ID is numeric
                if not StudentID.get().isdigit():
                    tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                else:
                    # Check if Mobile number is numeric and has exactly 10 digits
                    if not Mobile.get().isdigit() or len(Mobile.get()) != 10:
                        tkinter.messagebox.showerror("MySql Connection",
                                                     "Mobile number must be a 10-digit numeric value.")
                    else:
                        # Connect to the database and insert data
                        try:
                            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",database="final_project")
                            cur = sqlCon.cursor()
                            # Insert data into the database
                            cur.execute("INSERT INTO student_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                StudentID.get(),
                                Firstname.get(),
                                Surname.get(),
                                YearofStudy.get(),
                                DOB.get(),
                                roll.get(),
                                Mobile.get(),
                                Address.get(),
                                Gender.get(),
                                email.get()
                            ))
                            sqlCon.commit()
                            tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                        except pymysql.Error as e:
                            # Display error message if insertion fails
                            tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                        finally:
                            # Close the database connection
                            if 'sqlCon' in locals():
                                sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database
                with pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project") as sqlCon:
                    with sqlCon.cursor() as cur:
                        # Fetch data
                        cur.execute("""
                            SELECT student_details.*, semester_details.*, subject_details.*
                            FROM student_details
                            JOIN semester_details ON semester_details.student_id = student_details.student_id
                            JOIN subject_details ON subject_details.subject_id = semester_details.subject_id
                            WHERE subject_details.professor_id = %s
                        """, (self.username,))

                        result = cur.fetchall()

                        # If records found, clear the existing records and insert new ones
                        if len(result) != 0:
                            self.student_records.delete(*self.student_records.get_children())
                            for row in result:
                                self.student_records.insert("", END, values=row)
                        else:
                            tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except pymysql.Error as e:
                tkinter.messagebox.showerror("MySql Connection", f"Database error: {e}")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            StudentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            YearofStudy.set(row[3])
            DOB.set(row[4])
            roll.set(row[5])
            Mobile.set(row[6])
            Address.set(row[7])
            Gender.set(row[8])
            email.set(row[9])

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE student_details SET firstname=%s, lastname=%s, year=%s, date_of_birth=%s, roll_number=%s, contact_number=%s, address=%s, gender=%s, email=%s  WHERE student_id=%s",
                    (
                        Firstname.get(),
                        Surname.get(),
                        YearofStudy.get(),
                        DOB.get(),
                        roll.get(),
                        Mobile.get(),
                        Address.get(),
                        Gender.get(),
                        email.get(),
                        StudentID.get()
                    ))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM student_details WHERE student_id=%s", (StudentID.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT student_details.*, semester_details.*, subject_details.* "
                    "FROM student_details "
                    "JOIN semester_details ON student_details.student_id = semester_details.student_id "
                    "JOIN subject_details ON semester_details.subject_id = subject_details.subject_id "
                    "WHERE student_details.student_id = %s AND subject_details.professor_id = %s",
                    (StudentID.get(), self.username)
                )

                row = cur.fetchone()
                # Clear data displayed in the Treeview widget
                self.student_records.delete(*self.student_records.get_children())

                # If record found, fill entry fields with record data
                if row:
                    StudentID.set(row[0])
                    Firstname.set(row[1])
                    Surname.set(row[2])
                    YearofStudy.set(row[3])
                    DOB.set(row[4])
                    roll.set(row[5])
                    Mobile.set(row[6])
                    Address.set(row[7])
                    Gender.set(row[8])
                    email.set(row[9])
                    sqlCon.commit()
                    # Insert the searched record into the Treeview widget
                    self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        #----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # Student ID
        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',textvariable=StudentID)
        self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

        # Firstname
        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky="w", padx=5)
        self.entFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',textvariable=Firstname)
        self.entFirstname.grid(row=1, column=1, sticky="w", padx=5)

        # Surname
        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Lastname", bd=7)
        self.lblSurname.grid(row=2, column=0, sticky="w", padx=5)
        self.entSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',textvariable=Surname)
        self.entSurname.grid(row=2, column=1, sticky="w", padx=5)

        # year
        self.lblYearofStudy = Label(LeftFrame1, font=('arial', 12, 'bold'), text="YearofStudy", bd=5)
        self.lblYearofStudy.grid(row=3, column=0, sticky='w', padx=5)
        self.entYearofStudy = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=YearofStudy)
        self.entYearofStudy.grid(row=3, column=1, sticky=W, padx=5)

        # DOB
        self.lblDOB = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Date of Birth", bd=5)
        self.lblDOB.grid(row=4, column=0, sticky='w', padx=5)
        self.entDOB = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=DOB)
        self.entDOB.grid(row=4, column=1, sticky=W, padx=5)

        # roll
        self.lblroll = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Roll Number", bd=5)
        self.lblroll.grid(row=5, column=0, sticky='w', padx=5)
        self.entroll = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=roll)
        self.entroll.grid(row=5, column=1, sticky=W, padx=5)

        # Mobile
        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Mobile", bd=5)
        self.lblMobile.grid(row=6, column=0, sticky='w', padx=5)
        self.entMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=Mobile)
        self.entMobile.grid(row=6, column=1, sticky=W, padx=5)

        #address
        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Address", bd=7, )
        self.lblAddress.grid(row=7, column=0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=Address)
        self.entAddress.grid(row=7, column=1)

        # Gender
        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Gender", bd=5, )
        self.lblGender.grid(row=8, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state='readonly',textvariable=Gender)
        self.cboGender['values'] = (' ', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=8, column=1)

        #Email
        self.lblEmail = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Email", bd=5)
        self.lblEmail.grid(row=9, column=0, sticky='w', padx=5)
        self.entEmail = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=email)
        self.entEmail.grid(row=9, column=1, sticky=W, padx=5)

        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,columns=("stdid", "firstname", "surname", "year", "DOB", "roll","contact_number","address","gender","email"),
            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("stdid", text="studentID.")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("year", text="year")
        self.student_records.heading("DOB", text="DOB")
        self.student_records.heading("roll", text="roll")
        self.student_records.heading("contact_number", text="Mobile")
        self.student_records.heading("address", text="address")
        self.student_records.heading("gender", text="gender")
        self.student_records.heading("email", text="email")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("stdid", width=50)
        self.student_records.column("firstname", width=50)
        self.student_records.column("surname", width=50)
        self.student_records.column("year", width=50)
        self.student_records.column("DOB", width=50)
        self.student_records.column("roll", width=50)
        self.student_records.column("contact_number", width=50)
        self.student_records.column("address", width=50)
        self.student_records.column("gender", width=50)
        self.student_records.column("email", width=50)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)


class student_subject_details:

    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        StudentID = StringVar()
        name = StringVar()
        semester_number = StringVar()
        subject_id = StringVar()
        marks = StringVar()
        grade = StringVar()
        subject_name = StringVar()

        def exportData():
            try:
                # Open a file dialog for saving the CSV file
                filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if filename:
                    # Get the data from the Treeview widget
                    data = []
                    for child in self.student_records.get_children():
                        data.append(self.student_records.item(child)['values'])

                    # Write the data to the CSV file
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        # Write the header
                        writer.writerow(
                            ["Student ID", "Semester Number", "Subject ID", "Marks", "Grade", "Subject Name", "Name"])
                        # Write the data rows
                        writer.writerows(data)
                    tkinter.messagebox.showinfo("Export", "Data exported to CSV successfully.")
            except Exception as e:
                tkinter.messagebox.showerror("Export", f"Error: {e}")

        # ----------------------------------------------------------------------------------------------------
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageinstructor(login_window, self.username)

        # Function to exit the application

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields
            self.entStudentID.delete(0, END)
            self.entsemester_number.delete(0, END)
            self.entsubject_id.delete(0, END)
            self.entmarks.delete(0, END)
            self.entgrade.delete(0, END)
            self.entsubject_name.delete(0, END)
            self.entname.delete(0, END)

            # Clear data displayed in the Treeview widget
            self.student_records.delete(*self.student_records.get_children())

        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if StudentID.get() == "" or semester_number.get() == "" or subject_id.get() == "" or marks.get() == "" or grade.get() == "":
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Check if Student ID is numeric
                if not StudentID.get().isdigit():
                    tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                else:

                    # Connect to the database and insert data
                    try:
                        sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                                 database="final_project")
                        cur = sqlCon.cursor()
                        # Insert data into the database
                        cur.execute("INSERT INTO semester_details VALUES (%s, %s, %s, %s, %s)", (
                            StudentID.get(),
                            semester_number.get(),
                            subject_id.get(),
                            marks.get(),
                            grade.get(),
                        ))

                        sqlCon.commit()
                        tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                    except pymysql.Error as e:
                        # Display error message if insertion fails
                        tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                    finally:
                        # Close the database connection
                        if 'sqlCon' in locals():
                            sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database and fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT semester_details.student_id, semester_number, semester_details.subject_id, marks, grade, subject_name, "
                    "CONCAT(firstname, ' ', lastname) AS student_name "
                    "FROM semester_details "
                    "JOIN subject_details ON subject_details.subject_id = semester_details.subject_id "
                    "JOIN student_details ON student_details.student_id = semester_details.student_id "
                    "WHERE professor_id = %s", (self.username,)
                )

                result = cur.fetchall()
                # If records found, clear the existing records and insert new ones
                if len(result) != 0:
                    # Assuming self.student_records is your Treeview widget
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", tkinter.END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except pymysql.Error as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                try:
                    sqlCon.close()
                except NameError:
                    pass

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            StudentID.set(row[0])
            semester_number.set(row[1])
            subject_id.set(row[2])
            marks.set(row[3])
            grade.set(row[4])
            subject_name.set(row[5])
            name.set(row[6])

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE semester_details SET semester_number=%s, student_id=%s, marks=%s, grade=%s WHERE subject_id=%s AND student_id=%s",
                    (
                        semester_number.get(),
                        StudentID.get(),  # Fixed variable name here
                        marks.get(),
                        grade.get(),
                        subject_id.get(),
                        StudentID.get()  # Fixed variable name here
                    ))

                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM semester_details WHERE subject_id=%s", (subject_id.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            sqlCon = None
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT semester_details.student_id, semester_details.semester_number, semester_details.subject_id, "
                    "semester_details.marks, semester_details.grade, subject_details.subject_name, "
                    "CONCAT(student_details.firstname, ' ', student_details.lastname) AS name "
                    "FROM semester_details "
                    "JOIN subject_details ON subject_details.subject_id = semester_details.subject_id "
                    "JOIN student_details ON student_details.student_id = semester_details.student_id "
                    "WHERE semester_details.student_id = %s AND semester_details.subject_id = %s AND subject_details.professor_id = %s",
                    (StudentID.get(), subject_id.get(), self.username)
                )

                row = cur.fetchone()
                # If record found, fill entry fields with record data
                if row:
                    StudentID.set(row[0])
                    semester_number.set(row[1])
                    subject_id.set(row[2])
                    marks.set(row[3])
                    grade.set(row[4])
                    subject_name.set(row[5])
                    name.set(row[6])
                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        # ----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_subject_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # Student ID
        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=StudentID)
        self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

        # semester_number
        self.lblsemester_number = Label(LeftFrame1, font=('arial', 12, 'bold'), text="semester_number", bd=7)
        self.lblsemester_number.grid(row=1, column=0, sticky="w", padx=5)
        self.entsemester_number = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                        textvariable=semester_number)
        self.entsemester_number.grid(row=1, column=1, sticky="w", padx=5)

        # subject_id
        self.lblsubject_id = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_id", bd=7)
        self.lblsubject_id.grid(row=2, column=0, sticky="w", padx=5)
        self.entsubject_id = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=subject_id)
        self.entsubject_id.grid(row=2, column=1, sticky="w", padx=5)

        # marks
        self.lblmarks = Label(LeftFrame1, font=('arial', 12, 'bold'), text="marks", bd=5)
        self.lblmarks.grid(row=3, column=0, sticky='w', padx=5)
        self.entmarks = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=marks)
        self.entmarks.grid(row=3, column=1, sticky=W, padx=5)

        # grade
        self.lblgrade = Label(LeftFrame1, font=('arial', 12, 'bold'), text="grade", bd=5)
        self.lblgrade.grid(row=4, column=0, sticky='w', padx=5)
        self.entgrade = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=grade)
        self.entgrade.grid(row=4, column=1, sticky=W, padx=5)

        # grade
        self.lblsubject_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_name", bd=5)
        self.lblsubject_name.grid(row=5, column=0, sticky='w', padx=5)
        self.entsubject_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=subject_name)
        self.entsubject_name.grid(row=5, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="name", bd=5)
        self.lblname.grid(row=6, column=0, sticky='w', padx=5)
        self.entname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=name)
        self.entname.grid(row=6, column=1, sticky=W, padx=5)

        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12, columns=(
        "stdid", "semester_number", "subject_id", "marks", "grade", "subject_name", "name"),
                                            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("stdid", text="studentID.")
        self.student_records.heading("semester_number", text="semester_number")
        self.student_records.heading("subject_id", text="subject_id")
        self.student_records.heading("marks", text="marks")
        self.student_records.heading("grade", text="grade")
        self.student_records.heading("subject_name", text="subject_name")
        self.student_records.heading("name", text="name")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("stdid", width=65)
        self.student_records.column("semester_number", width=65)
        self.student_records.column("subject_id", width=60)
        self.student_records.column("marks", width=60)
        self.student_records.column("grade", width=55)
        self.student_records.column("subject_name", width=65)
        self.student_records.column("name", width=65)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        # Add Button
        # Add Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Add", bd=4, pady=1, padx=20, width=6,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Display", bd=4, pady=1, padx=20,
                                width=6, height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Update", bd=4, pady=1, padx=20,
                                width=6, height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Delete", bd=4, pady=1, padx=20,
                                width=6, height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Search", bd=4, pady=1, padx=20,
                                width=6, height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Reset", bd=4, pady=1, padx=20,
                                width=6, height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Back", bd=4, pady=1, padx=20,
                                width=6, height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 12, 'bold'), text="Export", bd=4, pady=1, padx=4,
                                width=8, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=3)


class student_project_details:

    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        StudentID = StringVar()
        project_name = StringVar()
        subject_id = StringVar()
        domain = StringVar()
        subject_name = StringVar()
        name = StringVar()

        # ----------------------------------------------------------------------------------------------------
        def exportData():
            try:
                # Open a file dialog for saving the CSV file
                filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if filename:
                    # Get the data from the Treeview widget
                    data = []
                    for child in self.student_records.get_children():
                        data.append(self.student_records.item(child)['values'])

                    # Write the data to the CSV file
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        # Write the header
                        writer.writerow(["Student ID", "Activity Name", "Name"])
                        # Write the data rows
                        writer.writerows(data)
                    messagebox.showinfo("Export", "Data exported to CSV successfully.")
            except Exception as e:
                messagebox.showerror("Export", f"Error: {e}")
        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageinstructor(login_window, self.username)

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields and StringVars
            entList = [self.entStudentID, self.entproject_name, self.entsubject_id, self.entdomain,
                       self.entsubject_name, self.lblname]
            for entry in entList:
                entry.delete(0, END)
            StudentID.set("")
            project_name.set("")
            subject_id.set("")
            domain.set("")
            subject_name.set("")
            name.set("")

            # Clear data displayed in the Treeview widget
            self.student_records.delete(*self.student_records.get_children())



        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if StudentID.get() == "" or project_name.get() == "" or subject_id.get() == "" or domain.get() == "":
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Check if Student ID is numeric
                if not StudentID.get().isdigit():
                    tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                else:

                    # Connect to the database and insert data
                    try:
                        sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                                 database="final_project")
                        cur = sqlCon.cursor()
                        # Insert data into the database
                        cur.execute("INSERT INTO project_details VALUES (%s, %s, %s, %s)", (
                            StudentID.get(),
                            project_name.get(),
                            subject_id.get(),
                            domain.get()
                        ))

                        sqlCon.commit()
                        tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                    except pymysql.Error as e:
                        # Display error message if insertion fails
                        tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                    finally:
                        # Close the database connection
                        if 'sqlCon' in locals():
                            sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database and fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT project_details.student_id, project_name, project_details.subject_id, domain, subject_name, CONCAT(firstname, ' ', lastname) "
                    "FROM project_details "
                    "JOIN subject_details ON subject_details.subject_id = project_details.subject_id "
                    "JOIN student_details ON student_details.student_id = project_details.student_id where professor_id = %s",self.username)

                result = cur.fetchall()
                # If records found, clear the existing records and insert new ones
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            if row:
                if len(row) >= 5:  # Check if row has enough elements
                    StudentID.set(row[0])
                    project_name.set(row[1])
                    subject_id.set(row[2])
                    domain.set(row[3])
                    subject_name.set(row[4])
                    name.set(row[5])

                else:
                    tkinter.messagebox.showerror("Error", "Invalid row data.")
            else:
                tkinter.messagebox.showerror("Error", "No row data.")

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE project_details SET project_name=%s, subject_id=%s, domain=%s WHERE student_id=%s",
                    (
                        project_name.get(),
                        subject_id.get(),
                        domain.get(),
                        StudentID.get()
                    ))

                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM project_details WHERE student_id=%s", (StudentID.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT project_details.student_id, project_name, project_details.subject_id, domain, subject_name, CONCAT(firstname, ' ', lastname) FROM project_details "
                    "JOIN subject_details ON subject_details.subject_id = project_details.subject_id "
                    "JOIN student_details ON student_details.student_id = project_details.student_id "
                    "WHERE project_details.student_id = %s and project_details.subject_id = %s",
                    (StudentID.get(), subject_id.get()))

                row = cur.fetchone()
                # If record found, fill entry fields with record data
                if row:
                    StudentID.set(row[0])
                    project_name.set(row[1])
                    subject_id.set(row[2])
                    domain.set(row[3])
                    subject_name.set(row[4])
                    name.set(row[5])
                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        # ----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_project_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # Student ID
        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=StudentID)
        self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

        # project_name
        self.lblproject_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="project_name", bd=7)
        self.lblproject_name.grid(row=1, column=0, sticky="w", padx=5)
        self.entproject_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                     textvariable=project_name)
        self.entproject_name.grid(row=1, column=1, sticky="w", padx=5)

        # subject_id
        self.lblsubject_id = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_id", bd=7)
        self.lblsubject_id.grid(row=2, column=0, sticky="w", padx=5)
        self.entsubject_id = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=subject_id)
        self.entsubject_id.grid(row=2, column=1, sticky="w", padx=5)

        # domain
        self.lbldomain = Label(LeftFrame1, font=('arial', 12, 'bold'), text="domain", bd=5)
        self.lbldomain.grid(row=3, column=0, sticky='w', padx=5)
        self.entdomain = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=domain)
        self.entdomain.grid(row=3, column=1, sticky=W, padx=5)

        self.lblsubject_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_name", bd=5)
        self.lblsubject_name.grid(row=4, column=0, sticky='w', padx=5)
        self.entsubject_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=subject_name)
        self.entsubject_name.grid(row=4, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="name", bd=5)
        self.lblname.grid(row=5, column=0, sticky='w', padx=5)
        self.lblname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44,
                             textvariable=name)
        self.lblname.grid(row=5, column=1, sticky=W, padx=5)

        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,
                                            columns=(
                                            "stdid", "project_name", "subject_id", "domain", "subject_name", "name"),
                                            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("stdid", text="studentID.")
        self.student_records.heading("project_name", text="project_name")
        self.student_records.heading("subject_id", text="subject_id")
        self.student_records.heading("domain", text="domain")
        self.student_records.heading("subject_name", text="subject_name")
        self.student_records.heading("name", text="name")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("stdid", width=80)
        self.student_records.column("project_name", width=80)
        self.student_records.column("subject_id", width=80)
        self.student_records.column("domain", width=80)
        self.student_records.column("subject_name", width=80)
        self.student_records.column("name", width=80)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        # Add Button
        # Add Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)


class student_activity_details:

    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(102 * " " + self.username)  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        self.StudentID = StringVar()
        self.activity = StringVar()
        self.name = StringVar()

        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageinstructor(login_window, self.username)

        def Reset():
            self.entStudentID.delete(0, END)
            self.entactivity_name.delete(0, END)
            self.entactivity_name_display.delete(0, END)

        def exportData():
            try:
                # Open a file dialog for saving the CSV file
                filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
                if filename:
                    # Get the data from the Treeview widget
                    data = []
                    for child in self.student_records.get_children():
                        data.append(self.student_records.item(child)['values'])

                    # Write the data to the CSV file
                    with open(filename, 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile)
                        # Write the header
                        writer.writerow(["Student ID", "Activity Name", "Name"])
                        # Write the data rows
                        writer.writerows(data)
                    tkinter.messagebox.showinfo("Export", "Data exported to CSV successfully.")
            except Exception as e:
                tkinter.messagebox.showerror("Export", f"Error: {e}")

        def addData():
            if self.StudentID.get() == "" or self.activity.get() == "":
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                if not self.StudentID.get().isdigit():
                    tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                else:
                    try:
                        sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                                 database="final_project")
                        cur = sqlCon.cursor()
                        cur.execute("INSERT INTO activity_details VALUES (%s, %s)", (
                            self.StudentID.get(),
                            self.activity.get()
                        ))

                        sqlCon.commit()
                        tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                    except pymysql.Error as e:
                        tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                    finally:
                        if 'sqlCon' in locals():
                            sqlCon.close()
                        self.DisplayData()

        def DisplayData():
            self.student_records.delete(*self.student_records.get_children())
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT activity_details.student_id, activity, CONCAT(firstname, ' ', lastname) "
                    "FROM activity_details "
                    "JOIN student_details ON student_details.student_id = activity_details.student_id "
                    "JOIN semester_details ON semester_details.student_id = student_details.student_id "
                    "JOIN subject_details ON semester_details.subject_id = subject_details.subject_id "
                    "WHERE professor_id = %s", (self.username,))

                result = cur.fetchall()
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        def Update():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE activity_details SET activity=%s WHERE student_id=%s",
                    (
                        self.activity.get(),
                        self.StudentID.get()
                    ))

                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()
                self.DisplayData()

        def Delete():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM activity_details WHERE student_id=%s", (self.StudentID.get(),))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                Reset()
                sqlCon.close()

        def searchDB():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT activity_details.*, CONCAT(firstname, ' ', lastname) AS name "
                    "FROM activity_details "
                    "JOIN semester_details ON semester_details.student_id = activity_details.student_id "
                    "JOIN student_details ON student_details.student_id = activity_details.student_id "
                    "JOIN subject_details ON subject_details.subject_id = semester_details.subject_id "
                    "WHERE activity_details.student_id = %s AND subject_details.professor_id = %s",
                    (self.StudentID.get(), self.username)
                )

                row = cur.fetchone()
                if row:
                    self.StudentID.set(row[0])
                    self.activity.set(row[1])
                    self.name.set(row[2])
                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()

                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_activity_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=self.StudentID)
        self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

        self.lblactivity_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Activity Name", bd=7)
        self.lblactivity_name.grid(row=1, column=0, sticky="w", padx=5)
        self.entactivity_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=self.activity)
        self.entactivity_name.grid(row=1, column=1, sticky="w", padx=5)

        self.lblactivity_name_display = Label(LeftFrame1, font=('arial', 12, 'bold'), text="name", bd=7)
        self.lblactivity_name_display.grid(row=2, column=0, sticky="w", padx=5)
        self.entactivity_name_display = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                              textvariable=self.name)
        self.entactivity_name_display.grid(row=2, column=1, sticky="w", padx=5)

        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,
                                            columns=("stdid", "activity_name","name"),
                                            yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text="Student ID")
        self.student_records.heading("activity_name", text="Activity Name")
        self.student_records.heading("name", text="name")
        self.student_records['show'] = 'headings'

        self.student_records.column("stdid", width=100)

        self.student_records.column("activity_name", width=100)
        self.student_records.column("name", width=100)

        self.student_records.pack(fill=BOTH, expand=1)

        self.student_records.bind("<ButtonRelease-1>", self.StudentInfo)

        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)

    def StudentInfo(self, ev):
        viewInfo = self.student_records.focus()
        learnerData = self.student_records.item(viewInfo)
        row = learnerData['values']
        if row:
            self.StudentID.set(row[0])
            self.activity.set(row[1])
            self.name.set(row[2])


class student_faculty_details:

    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(102 * " " + self.username)
        self.root.geometry("790x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2, relief="ridge")
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, relief="ridge")
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4, relief="ridge")
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, relief="ridge")
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2, relief="ridge")
        RightFrame1.pack(side="top")

        # Global variables
        subject_id = StringVar()
        professor = StringVar()
        credits = StringVar()
        subject_name = StringVar()

        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageinstructor(login_window, self.username)

        # Function to reset all entry fields
        def Reset():
            self.entsubject_id.delete(0, END)
            self.entprofessor.delete(0, END)
            self.entcredits.delete(0, END)
            self.entname.delete(0, END)
            self.student_records.delete(*self.student_records.get_children())


        # Function to display data from the database
        def DisplayData():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password", database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details")
                result = cur.fetchall()
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            subject_id.set(row[0])
            professor.set(row[1])
            credits.set(row[2])
            subject_name.set(row[3])

        # Function to search for a record in the database
        def searchDB():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password", database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT subject_id,professor,credits,subject_name FROM subject_details WHERE subject_id=%s", subject_id.get())

                row = cur.fetchone()
                if row:
                    subject_id.set(row[0])
                    professor.set(row[1])
                    credits.set(row[2])
                    subject_name.set(row[3])
                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_faculty_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # subject_id
        self.lblsubject_id = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_id", bd=7)
        self.lblsubject_id.grid(row=0, column=0, sticky="w", padx=5)
        self.entsubject_id = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=subject_id)
        self.entsubject_id.grid(row=0, column=1, sticky="w", padx=5)

        # professor
        self.lblprofessor = Label(LeftFrame1, font=('arial', 12, 'bold'), text="professor", bd=7)
        self.lblprofessor.grid(row=1, column=0, sticky="w", padx=5)
        self.entprofessor = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left', textvariable=professor)
        self.entprofessor.grid(row=1, column=1, sticky="w", padx=5)

        # credits
        self.lblcredits = Label(LeftFrame1, font=('arial', 12, 'bold'), text="credits", bd=5)
        self.lblcredits.grid(row=2, column=0, sticky='w', padx=5)
        self.entcredits = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=credits)
        self.entcredits.grid(row=2, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_name", bd=5)
        self.lblname.grid(row=3, column=0, sticky='w', padx=5)
        self.entname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=subject_name)
        self.entname.grid(row=3, column=1, sticky=W, padx=5)

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,
                                            columns=("subdid", "professor", "credits", "subject_name","professor_id"),
                                            yscrollcommand=scroll_y.set)

        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("subdid", text="subdid")
        self.student_records.heading("professor", text="professor")
        self.student_records.heading("credits", text="credits")
        self.student_records.heading("subject_name", text="subject_name")
        self.student_records.heading("professor_id", text="professor_id")
        self.student_records['show'] = 'headings'

        self.student_records.column("subdid", width=100)
        self.student_records.column("professor", width=100)
        self.student_records.column("credits", width=100)
        self.student_records.column("subject_name", width=100)
        self.student_records.column("professor_id", width=100)

        self.student_records.pack(fill=BOTH, expand=1)

        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        # Display Button
        self.btnDisplay = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=DisplayData)
        self.btnDisplay.grid(row=0, column=0, padx=1)

        # Search Button
        self.btnSearch = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8, height=2, command=searchDB)
        self.btnSearch.grid(row=1, column=0, padx=1)

        # Reset Button
        self.btnReset = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                               width=8, height=2, command=Reset)
        self.btnReset.grid(row=2, column=0, padx=1)

        # Exit Button
        self.btnBack = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24, width=8,
                              height=2, command=back, bg="red")
        self.btnBack.grid(row=3, column=0, padx=1)



#-----------------------------------------------------------------------------------------------------------------------




#admin functions
class Student_activityDetailsWindowadminview:
        def __init__(self, root, username):
            self.root = root
            self.username = username
            self.root.title(102 * " " + self.username)  # Title of the window
            self.root.geometry("790x700+300+0")  # Window size and position
            self.root.resizable(width=False, height=False)  # Window size not resizable

            MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
            MainFrame.grid()

            TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
            TitleFrame.grid(row=0, column=0)

            TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                              relief="ridge")  # Top frame for containing other frames
            TopFrame3.grid(row=1, column=0)

            LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2,
                              relief="ridge")  # Left frame for main content
            LeftFrame.pack(side="left")

            LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                               relief="ridge")  # Sub-frame inside LeftFrame
            LeftFrame1.pack(side="top", padx=0, pady=0)

            RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                               relief="ridge")  # Right frame for auxiliary content
            RightFrame.pack(side="right")

            RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                                relief="ridge")  # Sub-frame inside RightFrame
            RightFrame1.pack(side="top")

            self.StudentID = StringVar()
            self.activity = StringVar()
            self.name = StringVar()

            def back():
                self.root.destroy()
                login_window = Tk()
                login_app = MainPageadmin(login_window, self.username)

            def Reset():
                self.entStudentID.delete(0, END)
                self.entactivity_name.delete(0, END)
                self.entactivity_name_display.delete(0, END)
                self.student_records.delete(*self.student_records.get_children())

            def addData():
                if self.StudentID.get() == "" or self.activity.get() == "":
                    tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
                else:
                    if not self.StudentID.get().isdigit():
                        tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                    else:
                        try:
                            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                                     database="final_project")
                            cur = sqlCon.cursor()
                            cur.execute("INSERT INTO activity_details VALUES (%s, %s)", (
                                self.StudentID.get(),
                                self.activity.get()
                            ))

                            sqlCon.commit()
                            tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                        except pymysql.Error as e:
                            tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                        finally:
                            if 'sqlCon' in locals():
                                sqlCon.close()
                            self.DisplayData()

            def DisplayData():
                self.student_records.delete(*self.student_records.get_children())
                try:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                             database="final_project")
                    cur = sqlCon.cursor()
                    cur.execute(
                        "SELECT activity_details.student_id, activity, CONCAT(firstname, ' ', lastname) FROM activity_details "
                        "JOIN student_details ON student_details.student_id = activity_details.student_id")

                    result = cur.fetchall()
                    if len(result) != 0:
                        self.student_records.delete(*self.student_records.get_children())
                        for row in result:
                            self.student_records.insert("", END, values=row)
                    else:
                        tkinter.messagebox.showinfo("MySql Connection", "No records found")
                except Exception as e:
                    tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                finally:
                    sqlCon.close()

            def Update():
                try:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                             database="final_project")
                    cur = sqlCon.cursor()
                    cur.execute(
                        "UPDATE activity_details SET activity=%s WHERE student_id=%s",
                        (
                            self.activity.get(),
                            self.StudentID.get()
                        ))

                    sqlCon.commit()
                    tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
                except Exception as e:
                    tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
                finally:
                    if 'sqlCon' in locals():
                        sqlCon.close()
                    self.DisplayData()

            def Delete():
                try:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                             database="final_project")
                    cur = sqlCon.cursor()
                    cur.execute("DELETE FROM activity_details WHERE student_id=%s", (self.StudentID.get(),))
                    sqlCon.commit()
                    tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
                except Exception as e:
                    tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                finally:
                    Reset()
                    sqlCon.close()

            def searchDB():
                try:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                             database="final_project")
                    cur = sqlCon.cursor()
                    cur.execute(
                        "SELECT activity_details.student_id, activity, CONCAT(firstname, ' ', lastname) AS name FROM activity_details "
                        "JOIN student_details ON student_details.student_id = activity_details.student_id WHERE activity_details.student_id=%s",
                        (self.StudentID.get(),)
                    )
                    row = cur.fetchone()
                    if row:
                        self.StudentID.set(row[0])
                        self.activity.set(row[1])
                        self.name.set(row[2])
                        # Update the treeview with the search result
                        self.student_records.delete(*self.student_records.get_children())
                        self.student_records.insert("", END, values=row)
                        sqlCon.commit()
                    else:
                        tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                        Reset()
                except pymysql.Error as e:
                    tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
                finally:
                    if sqlCon:
                        sqlCon.close()

            def exportData():
                try:
                    # Ask for file path
                    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                             filetypes=[("Excel files", "*.xlsx"),
                                                                        ("All files", "*.*")])
                    if file_path:
                        # Fetch data from Treeview
                        rows = [self.student_records.item(item)['values'] for item in
                                self.student_records.get_children()]
                        if not rows:
                            tkinter.messagebox.showinfo("Export Data", "No data available to export")
                            return

                        # Create a DataFrame and save it to Excel
                        df = pd.DataFrame(rows, columns=["Student ID", "Activity Name", "Name"])
                        df.to_excel(file_path, index=False)
                        tkinter.messagebox.showinfo("Export Data", "Data exported successfully")
                except Exception as e:
                    tkinter.messagebox.showerror("Export Data", f"Error: {e}")

            self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_activity_details", bd=7)
            self.lbltitle.grid(row=0, column=0, padx=132)

            self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
            self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
            self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                      textvariable=self.StudentID)
            self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

            self.lblactivity_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Activity Name", bd=7)
            self.lblactivity_name.grid(row=1, column=0, sticky="w", padx=5)
            self.entactivity_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                          textvariable=self.activity)
            self.entactivity_name.grid(row=1, column=1, sticky="w", padx=5)

            self.lblactivity_name_display = Label(LeftFrame1, font=('arial', 12, 'bold'), text="name", bd=7)
            self.lblactivity_name_display.grid(row=2, column=0, sticky="w", padx=5)
            self.entactivity_name_display = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44,
                                                  justify='left',
                                                  textvariable=self.name)
            self.entactivity_name_display.grid(row=2, column=1, sticky="w", padx=5)

            scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
            self.student_records = ttk.Treeview(LeftFrame, height=12,
                                                columns=("stdid", "activity_name", "name"),
                                                yscrollcommand=scroll_y.set)

            scroll_y.pack(side=RIGHT, fill=Y)

            self.student_records.heading("stdid", text="Student ID")
            self.student_records.heading("activity_name", text="Activity Name")
            self.student_records.heading("name", text="name")
            self.student_records['show'] = 'headings'

            self.student_records.column("stdid", width=100)
            self.student_records.column("activity_name", width=100)
            self.student_records.column("name", width=100)

            self.student_records.pack(fill=BOTH, expand=1)

            self.student_records.bind("<ButtonRelease-1>", self.StudentInfo)

            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                    height=2, command=addData)
            self.btnAddNew.grid(row=0, column=0, padx=1)

            # Display Button
            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                    width=8,
                                    height=2, command=DisplayData)
            self.btnAddNew.grid(row=1, column=0, padx=1)

            # Update Button
            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                    width=8,
                                    height=2, command=Update)
            self.btnAddNew.grid(row=2, column=0, padx=1)

            # Delete Button
            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                    width=8,
                                    height=2, command=Delete)
            self.btnAddNew.grid(row=3, column=0, padx=1)

            # Search Button
            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                    width=8,
                                    height=2, command=searchDB)
            self.btnAddNew.grid(row=4, column=0, padx=1)

            # Reset Button
            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                    width=8,
                                    height=2, command=Reset)
            self.btnAddNew.grid(row=5, column=0, padx=1)

            # Exit Button
            self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                    width=8,
                                    height=2, command=back, bg="red")
            self.btnAddNew.grid(row=6, column=0, padx=1)

            self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                    width=12, height=2, command=exportData)
            self.btnExport.grid(row=7, column=0, padx=1, pady=5)

        def StudentInfo(self, event):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            self.StudentID.set(row[0])
            self.activity.set(row[1])
            self.name.set(row[2])


class Student_projectDetailsWindowadminview:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        StudentID = StringVar()
        project_name = StringVar()
        subject_id = StringVar()
        domain = StringVar()
        subject_name = StringVar()
        name = StringVar()

        # ----------------------------------------------------------------------------------------------------

        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageadmin(login_window, self.username)

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields and StringVars
            entList = [self.entStudentID, self.entproject_name, self.entsubject_id, self.entdomain,
                       self.entsubject_name, self.lblname]
            for entry in entList:
                entry.delete(0, END)
            StudentID.set("")
            project_name.set("")
            subject_id.set("")
            domain.set("")
            subject_name.set("")
            name.set("")
            self.student_records.delete(*self.student_records.get_children())


        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if StudentID.get() == "" or project_name.get() == "" or subject_id.get() == "" or domain.get() == "":
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Check if Student ID is numeric
                if not StudentID.get().isdigit():
                    tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                else:

                    # Connect to the database and insert data
                    try:
                        sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                                 database="final_project")
                        cur = sqlCon.cursor()
                        # Insert data into the database
                        cur.execute("INSERT INTO project_details VALUES (%s, %s, %s, %s)", (
                            StudentID.get(),
                            project_name.get(),
                            subject_id.get(),
                            domain.get()
                        ))

                        sqlCon.commit()
                        tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                    except pymysql.Error as e:
                        # Display error message if insertion fails
                        tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                    finally:
                        # Close the database connection
                        if 'sqlCon' in locals():
                            sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database and fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT project_details.student_id, project_name, project_details.subject_id, domain, subject_name, CONCAT(firstname, ' ', lastname) "
                    "FROM project_details "
                    "JOIN subject_details ON subject_details.subject_id = project_details.subject_id "
                    "JOIN student_details ON student_details.student_id = project_details.student_id")

                result = cur.fetchall()
                # If records found, clear the existing records and insert new ones
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            if row:
                if len(row) >= 5:  # Check if row has enough elements
                    StudentID.set(row[0])
                    project_name.set(row[1])
                    subject_id.set(row[2])
                    domain.set(row[3])
                    subject_name.set(row[4])
                    name.set(row[5])

                else:
                    tkinter.messagebox.showerror("Error", "Invalid row data.")
            else:
                tkinter.messagebox.showerror("Error", "No row data.")

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE project_details SET project_name=%s, subject_id=%s, domain=%s WHERE student_id=%s",
                    (
                        project_name.get(),
                        subject_id.get(),
                        domain.get(),
                        StudentID.get()
                    ))

                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM project_details WHERE student_id=%s", (StudentID.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "SELECT project_details.student_id, project_name, project_details.subject_id, domain, subject_name, CONCAT(firstname, ' ', lastname) FROM project_details "
                    "JOIN subject_details ON subject_details.subject_id = project_details.subject_id "
                    "JOIN student_details ON student_details.student_id = project_details.student_id "
                    "WHERE project_details.student_id = %s and project_details.subject_id = %s",
                    (StudentID.get(), subject_id.get()))

                row = cur.fetchone()
                # If record found, fill entry fields with record data
                if row:
                    StudentID.set(row[0])
                    project_name.set(row[1])
                    subject_id.set(row[2])
                    domain.set(row[3])
                    subject_name.set(row[4])
                    name.set(row[5])

                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        def exportData():
            try:
                # Get the file path using file dialog
                file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

                # Get data from Treeview widget
                tree_data = []
                for child in self.student_records.get_children():
                    tree_data.append(self.student_records.item(child)['values'])

                # Create a DataFrame from the data
                df = pd.DataFrame(tree_data,
                                  columns=["Student ID", "Project Name", "Subject ID", "Domain", "Subject Name",
                                           "Name"])

                # Export DataFrame to Excel
                df.to_excel(file_path, index=False)

                # Show success message
                tkinter.messagebox.showinfo("Export to Excel", "Data exported to Excel successfully.")
            except Exception as e:
                tkinter.messagebox.showerror("Export to Excel", f"Error: {e}")
        # ----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_project_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # Student ID
        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=StudentID)
        self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

        # project_name
        self.lblproject_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="project_name", bd=7)
        self.lblproject_name.grid(row=1, column=0, sticky="w", padx=5)
        self.entproject_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                     textvariable=project_name)
        self.entproject_name.grid(row=1, column=1, sticky="w", padx=5)

        # subject_id
        self.lblsubject_id = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_id", bd=7)
        self.lblsubject_id.grid(row=2, column=0, sticky="w", padx=5)
        self.entsubject_id = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=subject_id)
        self.entsubject_id.grid(row=2, column=1, sticky="w", padx=5)

        # domain
        self.lbldomain = Label(LeftFrame1, font=('arial', 12, 'bold'), text="domain", bd=5)
        self.lbldomain.grid(row=3, column=0, sticky='w', padx=5)
        self.entdomain = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=domain)
        self.entdomain.grid(row=3, column=1, sticky=W, padx=5)

        self.lblsubject_name = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_name", bd=5)
        self.lblsubject_name.grid(row=4, column=0, sticky='w', padx=5)
        self.entsubject_name = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=subject_name)
        self.entsubject_name.grid(row=4, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="name", bd=5)
        self.lblname.grid(row=5, column=0, sticky='w', padx=5)
        self.lblname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44,
                             textvariable=name)
        self.lblname.grid(row=5, column=1, sticky=W, padx=5)



        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,
                                            columns=(
                                            "stdid", "project_name", "subject_id", "domain", "subject_name", "name"),
                                            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("stdid", text="studentID.")
        self.student_records.heading("project_name", text="project_name")
        self.student_records.heading("subject_id", text="subject_id")
        self.student_records.heading("domain", text="domain")
        self.student_records.heading("subject_name", text="subject_name")
        self.student_records.heading("name", text="name")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("stdid", width=80)
        self.student_records.column("project_name", width=80)
        self.student_records.column("subject_id", width=80)
        self.student_records.column("domain", width=80)
        self.student_records.column("subject_name", width=80)
        self.student_records.column("name", width=80)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        # Add Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)


class Student_basicDetailsWindowadminview:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Update title to include username  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        StudentID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()
        YearofStudy = StringVar()
        DOB = StringVar()
        email = StringVar()
        roll = StringVar()

        # ----------------------------------------------------------------------------------------------------
        def exportData():
            try:
                # Get the file path using file dialog
                file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')

                # Get data from Treeview widget
                tree_data = []
                for child in self.student_records.get_children():
                    tree_data.append(self.student_records.item(child)['values'])

                # Create a DataFrame from the data
                df = pd.DataFrame(tree_data,
                                  columns=["Student ID", "Firstname", "Surname", "YearofStudy", "DOB", "Roll Number",
                                           "Mobile", "Address", "Gender", "Email"])

                # Export DataFrame to Excel
                df.to_excel(file_path, index=False)

                # Show success message
                messagebox.showinfo("Export to Excel", "Data exported to Excel successfully.")
            except Exception as e:
                messagebox.showerror("Export to Excel", f"Error: {e}")
        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageadmin(login_window, self.username)  # Pass the username to MainPageinstructor

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields
            self.entStudentID.delete(0, END)
            self.entFirstname.delete(0, END)
            self.entSurname.delete(0, END)
            self.entAddress.delete(0, END)
            self.cboGender.set('')
            self.entMobile.delete(0, END)
            self.entYearofStudy.delete(0, END)
            self.entDOB.delete(0, END)
            self.entEmail.delete(0, END)
            self.entroll.delete(0, END)
            self.student_records.delete(*self.student_records.get_children())


        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if StudentID.get() == "" or Firstname.get() == "" or Surname.get() == "" or Mobile.get() == "" or YearofStudy.get() == "" or DOB.get() == "" or email.get() == "":
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Check if Student ID is numeric
                if not StudentID.get().isdigit():
                    tkinter.messagebox.showerror("MySql Connection", "Student ID must be numeric.")
                else:
                    # Check if Mobile number is numeric and has exactly 10 digits
                    if not Mobile.get().isdigit() or len(Mobile.get()) != 10:
                        tkinter.messagebox.showerror("MySql Connection",
                                                     "Mobile number must be a 10-digit numeric value.")
                    else:
                        # Connect to the database and insert data
                        try:
                            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                                     database="final_project")
                            cur = sqlCon.cursor()
                            # Insert data into the database
                            cur.execute("INSERT INTO student_details VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                StudentID.get(),
                                Firstname.get(),
                                Surname.get(),
                                YearofStudy.get(),
                                DOB.get(),
                                roll.get(),
                                Mobile.get(),
                                Address.get(),
                                Gender.get(),
                                email.get()
                            ))
                            sqlCon.commit()
                            tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                        except pymysql.Error as e:
                            # Display error message if insertion fails
                            tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                        finally:
                            # Close the database connection
                            if 'sqlCon' in locals():
                                sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database and fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM student_details")
                result = cur.fetchall()
                # If records found, clear the existing records and insert new ones
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            StudentID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            YearofStudy.set(row[3])
            DOB.set(row[4])
            roll.set(row[5])
            Mobile.set(row[6])
            Address.set(row[7])
            Gender.set(row[8])
            email.set(row[9])

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE student_details SET firstname=%s, lastname=%s, year=%s, date_of_birth=%s, roll_number=%s, contact_number=%s, address=%s, gender=%s, email=%s  WHERE student_id=%s",
                    (
                        Firstname.get(),
                        Surname.get(),
                        YearofStudy.get(),
                        DOB.get(),
                        roll.get(),
                        Mobile.get(),
                        Address.get(),
                        Gender.get(),
                        email.get(),
                        StudentID.get()
                    ))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM student_details WHERE student_id=%s", (StudentID.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM student_details WHERE student_id=%s", StudentID.get())
                row = cur.fetchone()
                # If record found, fill entry fields with record data
                if row:
                    StudentID.set(row[0])
                    Firstname.set(row[1])
                    Surname.set(row[2])
                    YearofStudy.set(row[3])
                    DOB.set(row[4])
                    roll.set(row[5])
                    Mobile.set(row[6])
                    Address.set(row[7])
                    Gender.set(row[8])
                    email.set(row[9])

                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        # ----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # Student ID
        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=0, column=0, sticky="w", padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=StudentID)
        self.entStudentID.grid(row=0, column=1, sticky="w", padx=5)

        # Firstname
        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=1, column=0, sticky="w", padx=5)
        self.entFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=Firstname)
        self.entFirstname.grid(row=1, column=1, sticky="w", padx=5)

        # Surname
        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Lastname", bd=7)
        self.lblSurname.grid(row=2, column=0, sticky="w", padx=5)
        self.entSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                textvariable=Surname)
        self.entSurname.grid(row=2, column=1, sticky="w", padx=5)

        # year
        self.lblYearofStudy = Label(LeftFrame1, font=('arial', 12, 'bold'), text="YearofStudy", bd=5)
        self.lblYearofStudy.grid(row=3, column=0, sticky='w', padx=5)
        self.entYearofStudy = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=YearofStudy)
        self.entYearofStudy.grid(row=3, column=1, sticky=W, padx=5)

        # DOB
        self.lblDOB = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Date of Birth", bd=5)
        self.lblDOB.grid(row=4, column=0, sticky='w', padx=5)
        self.entDOB = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=DOB)
        self.entDOB.grid(row=4, column=1, sticky=W, padx=5)

        # roll
        self.lblroll = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Roll Number", bd=5)
        self.lblroll.grid(row=5, column=0, sticky='w', padx=5)
        self.entroll = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=roll)
        self.entroll.grid(row=5, column=1, sticky=W, padx=5)

        # Mobile
        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Mobile", bd=5)
        self.lblMobile.grid(row=6, column=0, sticky='w', padx=5)
        self.entMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=Mobile)
        self.entMobile.grid(row=6, column=1, sticky=W, padx=5)

        # address
        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Address", bd=7, )
        self.lblAddress.grid(row=7, column=0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                textvariable=Address)
        self.entAddress.grid(row=7, column=1)

        # Gender
        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Gender", bd=5, )
        self.lblGender.grid(row=8, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state='readonly',
                                      textvariable=Gender)
        self.cboGender['values'] = (' ', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=8, column=1)

        # Email
        self.lblEmail = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Email", bd=5)
        self.lblEmail.grid(row=9, column=0, sticky='w', padx=5)
        self.entEmail = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=email)
        self.entEmail.grid(row=9, column=1, sticky=W, padx=5)

        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12, columns=(
        "stdid", "firstname", "surname", "year", "DOB", "roll", "contact_number", "address", "gender", "email"),
                                            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("stdid", text="studentID.")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("year", text="year")
        self.student_records.heading("DOB", text="DOB")
        self.student_records.heading("roll", text="roll")
        self.student_records.heading("contact_number", text="Mobile")
        self.student_records.heading("address", text="address")
        self.student_records.heading("gender", text="gender")
        self.student_records.heading("email", text="email")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("stdid", width=50)
        self.student_records.column("firstname", width=50)
        self.student_records.column("surname", width=50)
        self.student_records.column("year", width=50)
        self.student_records.column("DOB", width=50)
        self.student_records.column("roll", width=50)
        self.student_records.column("contact_number", width=50)
        self.student_records.column("address", width=50)
        self.student_records.column("gender", width=50)
        self.student_records.column("email", width=50)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        # Add Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)


class Student_subjectDetailsWindowadminview:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        subject_id = StringVar()
        professor = StringVar()
        credits = StringVar()
        subject_name = StringVar()

        # ----------------------------------------------------------------------------------------------------

        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageadmin(login_window, self.username)

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields
            self.entsubject_id.delete(0, END)
            self.entprofessor.delete(0, END)
            self.entcredits.delete(0, END)
            self.entname.delete(0, END)
            self.student_records.delete(*self.student_records.get_children())


        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if subject_id.get() == "" or professor.get() == "" or credits.get() == "" or subject_name.get() == "":
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Connect to the database and insert data
                try:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                             database="final_project")
                    cur = sqlCon.cursor()
                    # Insert data into the database
                    cur.execute("INSERT INTO subject_details VALUES (%s, %s, %s, %s)", (
                        subject_id.get(),
                        professor.get(),
                        credits.get(),
                        subject_name.get()
                    ))

                    sqlCon.commit()
                    tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                except pymysql.Error as e:
                    # Display error message if insertion fails
                    tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                finally:
                    # Close the database connection
                    if 'sqlCon' in locals():
                        sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database and fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details")
                result = cur.fetchall()
                # If records found, clear the existing records and insert new ones
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            subject_id.set(row[0])
            professor.set(row[1])
            credits.set(row[2])
            subject_name.set(row[3])

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE subject_details SET professor=%s, credits=%s, subject_name=%s WHERE subject_id=%s",
                    (
                        professor.get(),
                        credits.get(),
                        subject_name.get(),
                        subject_id.get()
                    ))

                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM subject_details WHERE subject_id=%s", (subject_id.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details WHERE subject_id=%s", subject_id.get())

                row = cur.fetchone()
                # If record found, fill entry fields with record data
                if row:
                    subject_id.set(row[0])
                    professor.set(row[1])
                    credits.set(row[2])
                    subject_name.set(row[3])

                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        def exportData():
            try:
                # Open a file dialog to select the location to save the CSV file
                export_file_path = filedialog.asksaveasfilename(defaultextension='.csv',
                                                                filetypes=[("CSV files", '*.csv')])
                if not export_file_path:
                    return  # Exit if no file path is selected

                # Connect to the database to fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details")
                result = cur.fetchall()

                # Open the CSV file and write the data
                with open(export_file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    # Write the headers
                    writer.writerow(["Subject ID", "Professor", "Credits", "Subject Name"])
                    # Write the data rows
                    for row in result:
                        writer.writerow(row)

                messagebox.showinfo("Export Data", "Data exported successfully to " + export_file_path)

            except Exception as e:
                messagebox.showerror("Export Data", f"Error: {e}")

            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # ----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_faculty_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # subject_id
        self.lblsubject_id = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_id", bd=7)
        self.lblsubject_id.grid(row=0, column=0, sticky="w", padx=5)
        self.entsubject_id = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=subject_id)
        self.entsubject_id.grid(row=0, column=1, sticky="w", padx=5)

        # professor
        self.lblprofessor = Label(LeftFrame1, font=('arial', 12, 'bold'), text="professor", bd=7)
        self.lblprofessor.grid(row=1, column=0, sticky="w", padx=5)
        self.entprofessor = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=professor)
        self.entprofessor.grid(row=1, column=1, sticky="w", padx=5)

        # credits
        self.lblcredits = Label(LeftFrame1, font=('arial', 12, 'bold'), text="credits", bd=5)
        self.lblcredits.grid(row=2, column=0, sticky='w', padx=5)
        self.entcredits = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=credits)
        self.entcredits.grid(row=2, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_name", bd=5)
        self.lblname.grid(row=3, column=0, sticky='w', padx=5)
        self.entname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=subject_name)
        self.entname.grid(row=3, column=1, sticky=W, padx=5)

        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,
                                            columns=("subdid", "professor", "credits", "subject_name"),
                                            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("subdid", text="subdid")
        self.student_records.heading("professor", text="professor")
        self.student_records.heading("credits", text="credits")
        self.student_records.heading("subject_name", text="subject_name")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("subdid", width=100)
        self.student_records.column("professor", width=100)
        self.student_records.column("credits", width=100)
        self.student_records.column("subject_name", width=100)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        # Add Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)


class Student_semesterDetailsWindowadminview:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        titlespace = " "
        self.root.title(102 * " " + self.username)
        titlespace = " "
        self.root.title(102 * " " + self.username)  # Title of the window
        self.root.geometry("790x700+300+0")  # Window size and position
        self.root.resizable(width=False, height=False)  # Window size not resizable

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief="ridge", bg="cadet blue")  # Main frame
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief="ridge")  # Frame for the title section
        TitleFrame.grid(row=0, column=0)

        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Top frame for containing other frames
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2,
                          relief="ridge")  # Left frame for main content
        LeftFrame.pack(side="left")

        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, pady=4,
                           relief="ridge")  # Sub-frame inside LeftFrame
        LeftFrame1.pack(side="top", padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2,
                           relief="ridge")  # Right frame for auxiliary content
        RightFrame.pack(side="right")

        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2,
                            relief="ridge")  # Sub-frame inside RightFrame
        RightFrame1.pack(side="top")

        # global variables----------------------------------------------------------------------------------------------------

        subject_id = StringVar()
        professor = StringVar()
        credits = StringVar()
        subject_name = StringVar()

        # ----------------------------------------------------------------------------------------------------

        # Function to exit the application
        def back():
            self.root.destroy()
            login_window = Tk()
            login_app = MainPageadmin(login_window, self.username)

        # Function to reset all entry fields
        def Reset():
            # Clear all entry fields
            self.entsubject_id.delete(0, END)
            self.entprofessor.delete(0, END)
            self.entcredits.delete(0, END)
            self.entname.delete(0, END)
            self.student_records.delete(*self.student_records.get_children())

        def exportData():
            try:
                # Open a file dialog to select the location to save the CSV file
                export_file_path = filedialog.asksaveasfilename(defaultextension='.csv',
                                                                filetypes=[("CSV files", '*.csv')])
                if not export_file_path:
                    return  # Exit if no file path is selected

                # Connect to the database to fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details")
                result = cur.fetchall()

                # Open the CSV file and write the data
                with open(export_file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    # Write the headers
                    writer.writerow(["Subject ID", "Professor", "Credits", "Subject Name"])
                    # Write the data rows
                    for row in result:
                        writer.writerow(row)

                messagebox.showinfo("Export Data", "Data exported successfully to " + export_file_path)

            except Exception as e:
                messagebox.showerror("Export Data", f"Error: {e}")

            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to add new data to the database
        def addData():
            # Check if required fields are empty
            if subject_id.get() == "" or professor.get() == "" or credits.get() == "" or subject_name.get() == "":
                # Display an error message if any required field is empty
                tkinter.messagebox.showerror("MySql Connection", "Please fill in all required fields.")
            else:
                # Connect to the database and insert data
                try:
                    sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                             database="final_project")
                    cur = sqlCon.cursor()
                    # Insert data into the database
                    cur.execute("INSERT INTO subject_details VALUES (%s, %s, %s, %s)", (
                        subject_id.get(),
                        professor.get(),
                        credits.get(),
                        subject_name.get()
                    ))

                    sqlCon.commit()
                    tkinter.messagebox.showinfo("MySql Connection", "Record entered successfully.")
                except pymysql.Error as e:
                    # Display error message if insertion fails
                    tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
                finally:
                    # Close the database connection
                    if 'sqlCon' in locals():
                        sqlCon.close()

        # Function to display data from the database
        def DisplayData():
            try:
                # Connect to the database and fetch data
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details")
                result = cur.fetchall()
                # If records found, clear the existing records and insert new ones
                if len(result) != 0:
                    self.student_records.delete(*self.student_records.get_children())
                    for row in result:
                        self.student_records.insert("", END, values=row)
                else:
                    tkinter.messagebox.showinfo("MySql Connection", "No records found")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                sqlCon.close()

        # Function to fill entry fields when a student record is clicked
        def StudentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            subject_id.set(row[0])
            professor.set(row[1])
            credits.set(row[2])
            subject_name.set(row[3])

        # Function to update existing data in the database
        def Update():
            try:
                # Connect to the database and update record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute(
                    "UPDATE subject_details SET professor=%s, credits=%s, subject_name=%s WHERE subject_id=%s",
                    (
                        professor.get(),
                        credits.get(),
                        subject_name.get(),
                        subject_id.get()
                    ))

                sqlCon.commit()
                tkinter.messagebox.showinfo("MySQL Connection", "Record updated Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySQL Connection", f"Error: {e}")
            finally:
                if 'sqlCon' in locals():
                    sqlCon.close()

        # Function to delete a record from the database
        def Delete():
            try:
                # Connect to the database and delete record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("DELETE FROM subject_details WHERE subject_id=%s", (subject_id.get()))
                sqlCon.commit()
                tkinter.messagebox.showinfo("MySql Connection", "Record deleted Successfully")
            except Exception as e:
                tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")
            finally:
                # Reset entry fields after deletion
                Reset()
                sqlCon.close()

        # Function to search for a record in the database
        def searchDB():
            try:
                # Connect to the database and search for record
                sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                         database="final_project")
                cur = sqlCon.cursor()
                cur.execute("SELECT * FROM subject_details WHERE subject_id=%s", subject_id.get())

                row = cur.fetchone()
                # If record found, fill entry fields with record data
                if row:
                    subject_id.set(row[0])
                    professor.set(row[1])
                    credits.set(row[2])
                    subject_name.set(row[3])
                    # Update the treeview with the search result
                    self.student_records.delete(*self.student_records.get_children())
                    self.student_records.insert("", END, values=row)
                    sqlCon.commit()
                else:
                    tkinter.messagebox.showinfo("Data Entry Form", "No such record found")
                    # Reset entry fields if no record found
                    Reset()
            except pymysql.Error as e:
                tkinter.messagebox.showerror("Data Entry Form", f"Error: {e}")
            finally:
                if sqlCon:
                    sqlCon.close()

        # ----------------------------------------------------------------------------------------------------

        # Title
        self.lbltitle = Label(TitleFrame, font=('arial', 30, 'bold'), text="student_faculty_details", bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        # subject_id
        self.lblsubject_id = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_id", bd=7)
        self.lblsubject_id.grid(row=0, column=0, sticky="w", padx=5)
        self.entsubject_id = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                   textvariable=subject_id)
        self.entsubject_id.grid(row=0, column=1, sticky="w", padx=5)

        # professor
        self.lblprofessor = Label(LeftFrame1, font=('arial', 12, 'bold'), text="professor", bd=7)
        self.lblprofessor.grid(row=1, column=0, sticky="w", padx=5)
        self.entprofessor = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
                                  textvariable=professor)
        self.entprofessor.grid(row=1, column=1, sticky="w", padx=5)

        # credits
        self.lblcredits = Label(LeftFrame1, font=('arial', 12, 'bold'), text="credits", bd=5)
        self.lblcredits.grid(row=2, column=0, sticky='w', padx=5)
        self.entcredits = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=credits)
        self.entcredits.grid(row=2, column=1, sticky=W, padx=5)

        self.lblname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="subject_name", bd=5)
        self.lblname.grid(row=3, column=0, sticky='w', padx=5)
        self.entname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, textvariable=subject_name)
        self.entname.grid(row=3, column=1, sticky=W, padx=5)

        # ----------------------------------------------------------------------------------------------------

        # Scrollbar and Treeview widget for displaying student records
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records = ttk.Treeview(LeftFrame, height=12,
                                            columns=("subdid", "professor", "credits", "subject_name"),
                                            yscrollcommand=scroll_y.set)

        # Configure scrollbar to be packed to the right and fill the Y (vertical) direction
        scroll_y.pack(side=RIGHT, fill=Y)

        # Set headings for the columns in the student records Treeview
        self.student_records.heading("subdid", text="subdid")
        self.student_records.heading("professor", text="professor")
        self.student_records.heading("credits", text="credits")
        self.student_records.heading("subject_name", text="subject_name")
        self.student_records['show'] = 'headings'

        # Set widths for each column in the student records Treeview
        self.student_records.column("subdid", width=100)
        self.student_records.column("professor", width=100)
        self.student_records.column("credits", width=100)
        self.student_records.column("subject_name", width=100)

        # Pack the student records Treeview to fill both X (horizontal) and Y (vertical) directions and expand
        self.student_records.pack(fill=BOTH, expand=1)

        # Bind the "<ButtonRelease-1>" event to the StudentInfo function
        self.student_records.bind("<ButtonRelease-1>", StudentInfo)

        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Add", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData)
        self.btnAddNew.grid(row=0, column=0, padx=1)

        # Display Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=DisplayData)
        self.btnAddNew.grid(row=1, column=0, padx=1)

        # Update Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Update", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Update)
        self.btnAddNew.grid(row=2, column=0, padx=1)

        # Delete Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Delete", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Delete)
        self.btnAddNew.grid(row=3, column=0, padx=1)

        # Search Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Search", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=searchDB)
        self.btnAddNew.grid(row=4, column=0, padx=1)

        # Reset Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Reset", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=Reset)
        self.btnAddNew.grid(row=5, column=0, padx=1)

        # Exit Button
        self.btnAddNew = Button(RightFrame1, font=('arial', 16, 'bold'), text="Back", bd=4, pady=1, padx=24,
                                width=8,
                                height=2, command=back, bg="red")
        self.btnAddNew.grid(row=6, column=0, padx=1)

        self.btnExport = Button(RightFrame1, font=('arial', 16, 'bold'), text="Export", bd=4, pady=1, padx=6,
                                width=12, height=2, command=exportData)
        self.btnExport.grid(row=7, column=0, padx=1, pady=5)


#-----------------------------------------------------------------------------------------------------------------------

#student functions
class StudentActivityDisplayWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Student Activity Details")
        self.root.geometry("790x700+300+0")

        # Frame for displaying records
        self.display_frame = tkinter.Frame(self.root)
        self.display_frame.pack(pady=20)

        self.student_records = ttk.Treeview(self.display_frame, columns=("stdid", "activity_name","name"), height=15,
                                            show="headings")
        self.student_records.grid(row=0, column=0, padx=10, pady=10)

        scroll_y = tkinter.Scrollbar(self.display_frame, orient=tkinter.VERTICAL, command=self.student_records.yview)
        scroll_y.grid(row=0, column=1, sticky='ns')
        self.student_records.configure(yscrollcommand=scroll_y.set)

        self.student_records.heading("stdid", text="Student ID")
        self.student_records.heading("activity_name", text="Activity Name")
        self.student_records.heading("name", text="Name")

        # Frame for buttons below the display section
        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.back_button = tkinter.Button(self.button_frame, text="Back", font=('Arial', 14),
                                          command=self.back, bg="red", fg="white")
        self.back_button.pack(side="left", padx=10)

        # Fetch and display student activities
        self.fetch_student_activities()

    def back(self):
        self.root.destroy()
        login_window = tkinter.Tk()
        login_app = MainPagestudent(login_window, self.username)

    def fetch_student_activities(self):
        # Connect to the database and fetch activities for the given username
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()

            # Fetch data based on the student's username
            cur.execute("SELECT activity_details.student_id, activity, CONCAT(firstname, ' ', lastname) "
                        "FROM activity_details JOIN student_details ON student_details.student_id = activity_details.student_id "
                        "WHERE activity_details.student_id = %s", (self.username,))

            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.student_records.insert("", tkinter.END, values=row)
            else:
                tkinter.messagebox.showinfo("MySql Connection", "No activity records found for this user.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

class StudentDetailsDisplayWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Student Details")
        self.root.geometry("790x700+300+0")

        # Frame for displaying records
        self.display_frame = tkinter.Frame(self.root)
        self.display_frame.pack(pady=20)

        self.student_records = ttk.Treeview(self.display_frame, columns=(
            "student_id", "firstname", "lastname", "year", "date_of_birth", "roll_number", "contact_number", "address",
            "gender", "email"), height=15, show="headings")
        self.student_records.grid(row=0, column=0, padx=10, pady=10)

        scroll_y = tkinter.Scrollbar(self.display_frame, orient=tkinter.VERTICAL, command=self.student_records.yview)
        scroll_y.grid(row=0, column=1, sticky='ns')
        self.student_records.configure(yscrollcommand=scroll_y.set)

        self.student_records.heading("student_id", text="Student ID", anchor=tkinter.CENTER)
        self.student_records.heading("firstname", text="First Name", anchor=tkinter.CENTER)
        self.student_records.heading("lastname", text="Last Name", anchor=tkinter.CENTER)
        self.student_records.heading("year", text="Year", anchor=tkinter.CENTER)
        self.student_records.heading("date_of_birth", text="Date of Birth", anchor=tkinter.CENTER)
        self.student_records.heading("roll_number", text="Roll Number", anchor=tkinter.CENTER)
        self.student_records.heading("contact_number", text="Contact Number", anchor=tkinter.CENTER)
        self.student_records.heading("address", text="Address", anchor=tkinter.CENTER)
        self.student_records.heading("gender", text="Gender", anchor=tkinter.CENTER)
        self.student_records.heading("email", text="Email", anchor=tkinter.CENTER)

        # Set column widths
        self.student_records.column("student_id", width=70)
        self.student_records.column("firstname", width=70)
        self.student_records.column("lastname", width=70)
        self.student_records.column("year", width=70)
        self.student_records.column("date_of_birth", width=70)
        self.student_records.column("roll_number", width=70)
        self.student_records.column("contact_number", width=70)
        self.student_records.column("address", width=70)
        self.student_records.column("gender", width=70)
        self.student_records.column("email", width=70)

        # Frame for buttons below the display section
        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.back_button = tkinter.Button(self.button_frame, text="Back", font=('Arial', 14),
                                          command=self.back, bg="red", fg="white")
        self.back_button.pack(side="left", padx=10)

        # Fetch and display student details
        self.fetch_student_details()

    def back(self):
        self.root.destroy()
        login_window = tkinter.Tk()
        login_app = MainPagestudent(login_window, self.username)

    def fetch_student_details(self):
        # Connect to the database and fetch details for the given username
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()

            # Fetch data based on the student's username
            cur.execute("SELECT * FROM student_details WHERE student_id = %s", (self.username,))

            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.student_records.insert("", tkinter.END, values=row)
            else:
                tkinter.messagebox.showinfo("MySql Connection", "No student records found.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

class ProjectDetailsDisplayWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Project Details")
        self.root.geometry("790x700+300+0")

        # Frame for displaying records
        self.display_frame = tkinter.Frame(self.root)
        self.display_frame.pack(pady=20)

        self.project_records = ttk.Treeview(self.display_frame, columns=("student_id", "project_name", "subject_id", "domain"), height=15,
                                            show="headings")
        self.project_records.grid(row=0, column=0, padx=10, pady=10)

        scroll_y = tkinter.Scrollbar(self.display_frame, orient=tkinter.VERTICAL, command=self.project_records.yview)
        scroll_y.grid(row=0, column=1, sticky='ns')
        self.project_records.configure(yscrollcommand=scroll_y.set)

        self.project_records.heading("student_id", text="Student ID", anchor=tkinter.CENTER)
        self.project_records.heading("project_name", text="Project Name", anchor=tkinter.CENTER)
        self.project_records.heading("subject_id", text="Subject ID", anchor=tkinter.CENTER)
        self.project_records.heading("domain", text="Domain", anchor=tkinter.CENTER)

        # Set column widths
        self.project_records.column("student_id", width=100)
        self.project_records.column("project_name", width=200)
        self.project_records.column("subject_id", width=100)
        self.project_records.column("domain", width=200)

        # Frame for buttons below the display section
        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.back_button = tkinter.Button(self.button_frame, text="Back", font=('Arial', 14),
                                          command=self.back, bg="red", fg="white")
        self.back_button.pack(side="left", padx=10)

        # Fetch and display project details
        self.fetch_project_details()

    def back(self):
        self.root.destroy()
        login_window = tkinter.Tk()
        login_app = MainPagestudent(login_window, self.username)

    def fetch_project_details(self):
        # Connect to the database and fetch project details for the given username
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()

            # Fetch data based on the student's username
            cur.execute("SELECT * FROM project_details WHERE student_id = %s", (self.username,))

            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.project_records.insert("", tkinter.END, values=row)
            else:
                tkinter.messagebox.showinfo("MySql Connection", "No project records found.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

class SemesterDetailsDisplayWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Semester Details")
        self.root.geometry("790x700+300+0")

        # Frame for displaying records
        self.display_frame = tkinter.Frame(self.root)
        self.display_frame.pack(pady=20)

        self.semester_records = ttk.Treeview(self.display_frame, columns=("student_id", "semester_number", "subject_id", "marks", "grade", "subject_name"), height=15,
                                            show="headings")
        self.semester_records.grid(row=0, column=0, padx=10, pady=10)

        scroll_y = tkinter.Scrollbar(self.display_frame, orient=tkinter.VERTICAL, command=self.semester_records.yview)
        scroll_y.grid(row=0, column=1, sticky='ns')
        self.semester_records.configure(yscrollcommand=scroll_y.set)

        self.semester_records.heading("student_id", text="Student ID", anchor=tkinter.CENTER)
        self.semester_records.heading("semester_number", text="Semester Number", anchor=tkinter.CENTER)
        self.semester_records.heading("subject_id", text="Subject ID", anchor=tkinter.CENTER)
        self.semester_records.heading("marks", text="Marks", anchor=tkinter.CENTER)
        self.semester_records.heading("grade", text="Grade", anchor=tkinter.CENTER)
        self.semester_records.heading("subject_name", text="Subject Name", anchor=tkinter.CENTER)

        # Set column widths
        self.semester_records.column("student_id", width=100)
        self.semester_records.column("semester_number", width=100)
        self.semester_records.column("subject_id", width=100)
        self.semester_records.column("marks", width=100)
        self.semester_records.column("grade", width=100)
        self.semester_records.column("subject_name", width=100)

        # Frame for buttons below the display section
        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(pady=20)

        self.back_button = tkinter.Button(self.button_frame, text="Back", font=('Arial', 14),
                                          command=self.back, bg="red", fg="white")
        self.back_button.pack(side="left", padx=10)

        # Fetch and display semester details
        self.fetch_semester_details()

    def back(self):
        self.root.destroy()
        login_window = tkinter.Tk()
        login_app = MainPagestudent(login_window, self.username)

    def fetch_semester_details(self):
        # Connect to the database and fetch semester details for the given username
        try:
            sqlCon = pymysql.connect(host="localhost", user="root", password="your_db_password",
                                     database="final_project")
            cur = sqlCon.cursor()

            # Fetch data based on the student's username
            cur.execute(
                "SELECT student_id, semester_number, semester_details.subject_id, marks, grade, subject_name FROM "
                "semester_details JOIN subject_details ON subject_details.subject_id = semester_details.subject_id "
                "WHERE student_id = %s", (self.username,))

            result = cur.fetchall()
            if len(result) != 0:
                for row in result:
                    self.semester_records.insert("", tkinter.END, values=row)
            else:
                tkinter.messagebox.showinfo("MySql Connection", "No semester records found.")
        except pymysql.Error as e:
            tkinter.messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            if 'sqlCon' in locals():
                sqlCon.close()

class FacultyDetailsDisplayWindow:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Subject Details")
        self.root.geometry("790x700+300+0")

        self.search_frame = tkinter.Frame(self.root)
        self.search_frame.pack(pady=20)

        self.search_label = tkinter.Label(self.search_frame, text="Enter Subject ID:", font=('Arial', 14))
        self.search_label.grid(row=0, column=0, padx=10)

        self.search_entry = tkinter.Entry(self.search_frame, font=('Arial', 14), width=20)
        self.search_entry.grid(row=0, column=1, padx=10)

        self.search_button = tkinter.Button(self.search_frame, text="Search", font=('Arial', 14),
                                            command=self.search_subject, bg="#4DA8FF", fg="white")
        self.search_button.grid(row=0, column=2, padx=10)

        self.reset_button = tkinter.Button(self.search_frame, text="Reset", font=('Arial', 14),
                                           command=self.reset_fields, bg="gray", fg="white")
        self.reset_button.grid(row=0, column=3, padx=10)

        self.display_all_button = tkinter.Button(self.search_frame, text="Display All Data", font=('Arial', 14),
                                                 command=self.display_all_data, bg="#4DA8FF", fg="white")
        self.display_all_button.grid(row=0, column=4, padx=10)

        self.display_frame = tkinter.Frame(self.root)
        self.display_frame.pack(pady=20, padx=20, fill=tkinter.BOTH, expand=True)

        self.student_records = ttk.Treeview(self.display_frame, columns=("subject_id", "professor", "credits", "name"),
                                            height=20, show="headings")
        self.student_records.grid(row=0, column=0, padx=10, pady=10,
                                  sticky=(tkinter.N, tkinter.S, tkinter.E, tkinter.W))

        scroll_y = tkinter.Scrollbar(self.display_frame, orient=tkinter.VERTICAL, command=self.student_records.yview)
        scroll_y.grid(row=0, column=1, sticky=(tkinter.N, tkinter.S))
        self.student_records.configure(yscrollcommand=scroll_y.set)

        self.student_records.heading("subject_id", text="Subject ID")
        self.student_records.heading("professor", text="Professor")
        self.student_records.heading("credits", text="Credits")
        self.student_records.heading("name", text="Name")

        # Configure grid weights for resizing
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.rowconfigure(0, weight=1)

        # Adjust column widths
        self.student_records.column("subject_id", width=100)
        self.student_records.column("professor", width=150)
        self.student_records.column("credits", width=100)
        self.student_records.column("name", width=200)

        # Frame for buttons below the display section
        self.button_frame = tkinter.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.back_button = tkinter.Button(self.button_frame, text="Back", font=('Arial', 14),
                                           command=self.back, bg="red", fg="white")
        self.back_button.pack()

    def back(self):
        self.root.destroy()
        login_window = Tk()
        login_app = MainPagestudent(login_window, self.username)

    def search_subject(self):
        # Clear existing data
        for record in self.student_records.get_children():
            self.student_records.delete(record)

        # Connect to the database and fetch data
        try:
            conn = pymysql.connect(host="localhost", user="root", password="your_db_password", database="final_project")
            cursor = conn.cursor()

            # Fetch data based on the entered subject ID
            subject_id = self.search_entry.get()
            cursor.execute("SELECT * FROM subject_details WHERE subject_id = %s", (subject_id,))
            result = cursor.fetchall()
            if len(result) != 0:
                for row in result:
                    self.student_records.insert("", tkinter.END, values=row)
            else:
                tkinter.messagebox.showinfo("MySql Connection", "No records found")

        except pymysql.Error as e:
            tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")

        finally:
            # Close database connection
            if 'conn' in locals() and conn.open:
                cursor.close()
                conn.close()

    # Function to reset fields and clear data in the display section
    def reset_fields(self):
        # Clear search entry field
        self.search_entry.delete(0, tkinter.END)
        # Clear data in the display section
        for record in self.student_records.get_children():
            self.student_records.delete(record)

    # Function to display all data
    def display_all_data(self):
        # Clear existing data
        for record in self.student_records.get_children():
            self.student_records.delete(record)

        # Connect to the database and fetch all data
        try:
            conn = pymysql.connect(host="localhost", user="root", password="your_db_password", database="final_project")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM subject_details")
            result = cursor.fetchall()
            if len(result) != 0:
                for row in result:
                    self.student_records.insert("", tkinter.END, values=row)
            else:
                tkinter.messagebox.showinfo("MySql Connection", "No records found")

        except pymysql.Error as e:
            tkinter.messagebox.showerror("MySql Connection", f"Error: {e}")

        finally:
            # Close database connection
            if 'conn' in locals() and conn.open:
                cursor.close()
                conn.close()



#-----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    landing_root = Tk()
    landing_page = LandingPage(landing_root)
    landing_root.mainloop()
