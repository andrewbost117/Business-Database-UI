import sqlite3



# This function connects the database and returns it to main
def connect_database():
    con = sqlite3.connect("business.db")
    return con

# This is the main function
def main():

    # The Connection and Cursor Variables
    dbConnection = connect_database()
    cur = dbConnection.cursor()

    # Saves schema.sql into a string Python can read
    with open("schema.sql", "r") as schema_file:
        sql_script = schema_file.read()


    cur.executescript(sql_script)


    #name = input("Enter employee name: ")
    #id = input("Enter employee ID you'd wish to delete: ")

    #newname = input("Enter a new name: ")

    #create_employee(name)
    #employees = read_employee(id)
    #update_employee(id, newname)
    #delete_employee(id)

    #sql_query = "DELETE FROM Employees WHERE EmployeeID = ?"
    #target_id = 8
    #cur.execute(sql_query, (target_id,))
    #dbConnection.commit()


    dbConnection.close()

# The purpose of this function is to create an employee
def create_employee(employee_name):

    # Input validation: If not a string return   
    if not isinstance(employee_name, str):
        return False

    # Clear any extra space
    employee_name = employee_name.strip()

    # Input validation: If its an empty string return
    if employee_name == "":
        return False

    dbConnection = None
        
    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

            # Inserts the input into the database
            cur.execute("INSERT INTO Employees (Name) VALUES (?)", (employee_name,))
            inserted_id = cur.lastrowid

            # Returns the ID
            #print(f"The inserted row ID is : {inserted_id}")
            return inserted_id
        
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False

    finally:
        if dbConnection is not None:
            dbConnection.close()

# The purpose of this function is to read a specific employee
def read_employee():

    dbConnection = None

    # DB connection
    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

            # Gets all of the results in the Employees Table and saves them into 'results'
            res = cur.execute("SELECT * FROM employees")
            results = res.fetchall()
            
            #print(results)
            
            return results
        
    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False

    finally:
        if dbConnection is not None:
            dbConnection.close()

# The purpose of this function is to update an existing employee
def update_employee(employee_id, new_name):

    dbConnection = None

    # Input validation: If it isn't a string return    
    if not isinstance(new_name, str):
        return False
    

    # Clear any extra space
    new_name = new_name.strip()

    # Input validation: If it is an empty string return
    if new_name == "":
        return False

    # Input validation: Makes sure the Employee ID is legit if not returns
    if type(employee_id) is not int or employee_id <= 0:
        print("Invalid employee ID.")
        return False

    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

            # Parameterized SQL query for safety reasons
            query = "UPDATE Employees SET Name = ? WHERE EmployeeID = ?"

            # Parameters
            par = (new_name, employee_id)

            cur.execute(query, par)

            
            dbConnection.commit()
            return True

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False

    finally:
        if dbConnection is not None:
            dbConnection.close()

# The purpose of this funciton is to delete an existing employee 
def delete_employee(employee_id):

    dbConnection = None

   # Input validation: Makes sure the Employee ID is legit if not returns
    if type(employee_id) is not int or employee_id <= 0:
        print("Invalid employee ID.")
        return False



    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

       
            # Parameterized SQL query for safety reasons
            query = "DELETE FROM Employees WHERE EmployeeID = ?"

            # Parameters
            par = (employee_id,)

            cur.execute(query, par)

            if cur.rowcount == 0:
                print("Employee not found.")
            else:
                print("Employee deleted successfully.")

            dbConnection.commit()
            return True

    except sqlite3.Error as error:
        print(f"Database error: {error}")
        return False

    finally:
        if dbConnection is not None:
            dbConnection.close()


main()