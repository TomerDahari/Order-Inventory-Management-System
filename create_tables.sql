CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50) NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity >= 0)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerName NVARCHAR(100) NOT NULL,
    OrderDate DATETIME NOT NULL DEFAULT GETDATE(),
    StatusID INT FOREIGN KEY REFERENCES OrderStatus(StatusID)
);


CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT NOT NULL CHECK (Quantity > 0)
);

CREATE TABLE ProductHistory (
    HistoryID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT,
    ProductName NVARCHAR(100),
    Category NVARCHAR(50),
    Quantity INT,
    AddedDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


CREATE TABLE OrderStatus (
    StatusID INT PRIMARY KEY IDENTITY(1,1),
    StatusName NVARCHAR(50) NOT NULL
);


INSERT INTO OrderStatus (StatusName)
VALUES ('Pending'), ('In Process'), ('Shipped'), ('Delivered');


ALTER TABLE Orders
ADD StatusID INT FOREIGN KEY REFERENCES OrderStatus(StatusID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT;


CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(100) NOT NULL UNIQUE,
    Password NVARCHAR(100) NOT NULL
);
