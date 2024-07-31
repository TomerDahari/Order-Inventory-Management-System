-- äåñôú ðúåðé ãåâîä ìèáìú ì÷åçåú
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, PostalCode, Country)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', '12345', 'USA'),
('Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', '456 Elm St', 'Othertown', '67890', 'USA');

-- äåñôú ðúåðé ãåâîä ìèáìú ñô÷éí
INSERT INTO Suppliers (CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, HomePage)
VALUES 
('Acme Corp', 'Alice Johnson', 'Sales Manager', '789 Oak St', 'Sometown', 'Region1', '54321', 'USA', '345-678-9012', '345-678-9013', 'http://www.acme.com');

-- äåñôú ðúåðé ãåâîä ìèáìú ÷èâåøéåú
INSERT INTO Categories (CategoryName, Description)
VALUES 
('Beverages', 'Soft drinks, coffees, teas, beers, and ales'),
('Condiments', 'Sweet and savory sauces, relishes, spreads, and seasonings');

-- äåñôú ðúåðé ãåâîä ìèáìú îåöøéí
INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
VALUES 
('Chai', 1, 1, '10 boxes x 20 bags', 18.00, 39, 0, 10, 0),
('Chang', 1, 1, '24 - 12 oz bottles', 19.00, 17, 40, 25, 0);

-- äåñôú ðúåðé ãåâîä ìèáìú äæîðåú
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry)
VALUES 
(1, 1, '2024-01-01', '2024-01-08', '2024-01-03', 1, 29.99, 'John Doe', '123 Main St', 'Anytown', 'Region1', '12345', 'USA');

-- äåñôú ðúåðé ãåâîä ìèáìú ôøèé äæîðåú
INSERT INTO OrderDetails (OrderID, ProductID, UnitPrice, Quantity, Discount)
VALUES 
(1, 1, 18.00, 5, 0.1),
(1, 2, 19.00, 10, 0.05);
GO
