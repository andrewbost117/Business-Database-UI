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


    # name = input("Enter employee name: ")
    id = input("Enter employee ID: ")

    newname = input("Enter a new name: ")

    #create_employee(name)
    #employees = read_employee(id)
    update_employee(id, newname)

    #sql_query = ("UPDATE Employees SET Name = ? WHERE EmployeeID = ?")
    #data = ('Bob', 1)
    #cur.execute(sql_query, data)
    #dbConnection.commit()

    #sql_query = "DELETE FROM Employees WHERE EmployeeID = ?"
    #target_id = 8
    #cur.execute(sql_query, (target_id,))
    #dbConnection.commit()

    #res = cur.execute("SELECT EmployeeID, Name FROM Employees")
    #results = res.fetchall()
    #print(results)

    dbConnection.close()

def create_employee(employee_name):

    # Input validation: If not a string return   
    if not isinstance(employee_name, str):
        return

    # Clear any extra space
    employee_name = employee_name.strip()

    # Input validation: If its an empty string return
    if employee_name == "":
        return

    dbConnection = None
        
    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

            # Inserts the input into the database
            cur.execute("INSERT INTO Employees (Name) VALUES (?)", (employee_name,))
            inserted_id = cur.lastrowid

            # Returns the ID
            print(f"The inserted row ID is : {inserted_id}")
            return inserted_id
        
    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        if dbConnection is not None:
            dbConnection.close()

def read_employee(employee_id):

    dbConnection = None

    # DB connection
    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

            # Gets all of the results in the Employees Table and saves them into 'results'
            res = cur.execute("SELECT * FROM employees WHERE EmployeeID = ?", (employee_id,))
            results = res.fetchone()
            
            #print(results)
            
            return results
        
    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        if dbConnection is not None:
            dbConnection.close()

def update_employee(employee_id, new_name):

    dbConnection = None

    # Input validation: If it isn't a string return    
    if not isinstance(new_name, str):
        return

    # Clear any extra space
    new_name = new_name.strip()

    # Input validation: If it is an empty string return
    if new_name == "":
        return

    # Input validation: Makes sure the Employee ID is legit if not returns
    if type(employee_id) is not int or employee_id <= 0:
        print("Invalid employee ID.")
        return

    try: 
        with sqlite3.connect("business.db") as dbConnection:
            cur = dbConnection.cursor()

            # Parameterized SQL query for safety reasons
            query = "UPDATE Employees SET Name = ? WHERE EmployeeID = ?"

            # Parameters
            par = (new_name, employee_id)

            cur.execute(query, par)


            dbConnection.commit()

    except sqlite3.Error as error:
        print(f"Database error: {error}")

    finally:
        if dbConnection is not None:
            dbConnection.close()




main()