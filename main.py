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


    name = input("Enter employee name (3-15 Characters): ")


    create_employee(name)

    # Verifies that the new table is made by querying  
    #res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #results = res.fetchall()
    #print(results)



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

    # Input validation     
    if not isinstance(employee_name, str):
        return

    employee_name = employee_name.strip()

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

main()