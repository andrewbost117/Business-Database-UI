PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    Name       TEXT
);

CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name       TEXT
);

CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY,
    Name      TEXT,
    Price     NUMERIC
);

CREATE TABLE IF NOT EXISTS Orders (
    OrderID   INTEGER PRIMARY KEY,
    EmployeeID INTEGER,
    CustomerID INTEGER,
    ProductID INTEGER,
    Quantity  INTEGER,

    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID)  REFERENCES Products(ProductID)
);
