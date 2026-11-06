import customtkinter as ctk
import main


# This function creates new employees
def handle_create_employee():
    employee_name = employee_entry.get()

    employee_id = main.create_employee(employee_name)

    if employee_id is not None:
        status_label.configure(text="Employee created successfully.")
        employee_entry.delete(0, "end")
    else:
        status_label.configure(text="Failed to create employee.")

# This function prints all results in the employees table from the database
def handle_read_employees():
    # Calls the read employee function and saves the returned results into their own tuple, employees
    employees = main.read_employee()

    employee_textbox.delete("1.0", "end")

    # This iterates through each tuple and prints our the information into the textbox
    for employee in employees:
        employee_id = employee[0]
        employee_name = employee[1]
        employee_textbox.insert("end",f"Employee ID: {employee_id} | Employee Name: {employee_name}\n")

    status_label.configure(text="All Employees Successfully Displayed.")

# This function updates an existing employee 
def handle_update_employee():

    # Validates that the user input is a number
    try:
        employee_id = int(update_entry.get())
    except ValueError:
        status_label.configure(text="Please enter a valid employee ID.")
        return

    employee_new_name = update_name_entry.get()

    main.update_employee(employee_id, employee_new_name)
    status_label.configure(text="Employee Updated Successfully.")

# This function deletes an existing employees
def handle_delete_employee():
    # Validates that the user input is a number
    try:
        employee_id = int(delete_entry.get())

    except ValueError:
        status_label.configure(text="Please enter a valid employee ID.")
        return

    success = main.delete_employee(employee_id)
    if success:
        status_label.configure(text="Employee Deleted Successfully.")
    else:
        status_label.configure(text="Employee not found or deletion failed.")   

# This function changes the theme of the UI
def change_theme():
    status = check_var.get()
    print(status)
    if status == "Light":
        ctk.set_appearance_mode("Light")
    elif status == "Dark":
        ctk.set_appearance_mode("Dark")

def show_page(page):
    employees_frame.pack_forget()
    customers_frame.pack_forget()
    prodcuts_frame.pack_forget()
    orders_frame.pack_forget()

    page.pack(fill="both", expand=True)
# Creates the main application's window
app = ctk.CTk()

# Set the window title
app.title("Business Database App")

# Window Dimensions
app.geometry("800x800")
app.minsize(600, 650)


# FRAMES 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Side Bar and its children widgets for changing pages
sidebar_frame = ctk.CTkFrame(app, width=180, corner_radius=0)
sidebar_frame.pack(side="left",fill="y")
sidebar_frame.pack_propagate(False) # Prevents child widgets from changing the frame's requested dimensions

# Content frame 
content_frame = ctk.CTkFrame(app, fg_color="transparent")
content_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

employee_title_frame = ctk.CTkFrame(content_frame)
employee_title_frame.pack(fill="x",padx=10, pady=10)

# Frame for employees
employees_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
employees_frame.pack(fill="both", expand=True)

employees_frame.grid_columnconfigure(0, weight=1, uniform="crud")
employees_frame.grid_columnconfigure(1, weight=1, uniform="crud")

employees_frame.grid_rowconfigure(0, weight=1)
employees_frame.grid_rowconfigure(0, weight=1)

create_frame = ctk.CTkFrame(employees_frame)
create_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

read_frame = ctk.CTkFrame(employees_frame)
read_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

update_frame = ctk.CTkFrame(employees_frame)
update_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

delete_frame = ctk.CTkFrame(employees_frame)
delete_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")



# Frame for customers
customers_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
customers_frame.pack(fill="both", expand=True)

# Frame for products
prodcuts_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
prodcuts_frame.pack(fill="both", expand=True)

# Frame for orders
orders_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
orders_frame.pack(fill="both", expand=True)

# The program calls this to avoid any layout issues 
show_page(employees_frame)

# SIDE BAR WIDGETS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Employees Page Button
employees_button = ctk.CTkButton(sidebar_frame, text="Employees",command=lambda: show_page(employees_frame))
employees_button.pack(padx=10, pady=10, fill="x")

customers_button = ctk.CTkButton(sidebar_frame, text="Customers", command=lambda: show_page(customers_frame))
customers_button.pack(padx=10, pady=10, fill="x")

products_button = ctk.CTkButton(sidebar_frame, text="Products", command=lambda: show_page(prodcuts_frame))
products_button.pack(padx=10, pady=10, fill="x")

orders_button = ctk.CTkButton(sidebar_frame, text="Orders", command=lambda: show_page(orders_frame))
orders_button.pack(padx=10, pady=10, fill="x")

# EMPLOYEES WIDGETS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Employees Title 
employees_title = ctk.CTkLabel(employee_title_frame, text="Employee Management", font=("Arial",24))
employees_title.pack(pady=5)


# Checkbox for Theme changing
check_var = ctk.StringVar(value="Dark")
theme_checkbox = ctk.CTkCheckBox(master = sidebar_frame, text="Dark Mode", command=change_theme, variable=check_var, onvalue="Dark", offvalue="Light")
theme_checkbox.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")

# User input field for Create employee
employee_entry = ctk.CTkEntry(create_frame, placeholder_text="Enter Employee Name")
employee_entry.pack(pady=10)

# Create employee button
create_button = ctk.CTkButton(create_frame, text="Create Employee", command=handle_create_employee)
create_button.pack(pady=15)


# Button and Textbox for viewing all employees
view_title = ctk.CTkLabel(read_frame, text="Employee Records")
view_title.pack(pady=10)
employee_textbox = ctk.CTkTextbox(read_frame, width=350, height=120)
employee_textbox.pack(pady=10)
view_button = ctk.CTkButton(read_frame, text="View All Employees", command=handle_read_employees)
view_button.pack(pady=10)

# Status label 
status_label = ctk.CTkLabel(read_frame, text="")
status_label.pack(pady=10)

# Entry fields & button for updating an existing employee
update_title = ctk.CTkLabel(update_frame, text="Update Employee")
update_title.pack(pady=10)
update_entry = ctk.CTkEntry(update_frame, placeholder_text="Enter Employee ID")
update_entry.pack(pady=10)
update_name_entry = ctk.CTkEntry(update_frame, placeholder_text="Enter New Name")
update_name_entry.pack(pady=10)
update_button = ctk.CTkButton(update_frame, text="Modify Employee", command=handle_update_employee)
update_button.pack(pady=10)

# Entry field & button to delete an existing employee
delete_title = ctk.CTkLabel(delete_frame, text="Delete Employee")
delete_title.pack(pady=10)
delete_entry = ctk.CTkEntry(delete_frame, placeholder_text="Enter Employee ID")
delete_entry.pack(pady=10)
delete_button = ctk.CTkButton(delete_frame, text="Delete Employee", command=handle_delete_employee)
delete_button.pack(pady=10)

# CUSTROMERS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# PRODUCTS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ORDERS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Start the GUI event loop
app.mainloop()