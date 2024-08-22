SELECT 
    YEAR(OrderDate) AS OrderYear, 
    MONTH(OrderDate) AS OrderMonth,
    SUM((UnitPrice * Quantity) * (1 - Discount)) AS TotalSales
FROM Orders
JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
ORDER BY OrderYear, OrderMonth;


SELECT 
    ProductName, 
    UnitsInStock, 
    ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;
GO


SELECT 
    C.CustomerID, 
    C.FirstName, 
    C.LastName, 
    SUM((OD.UnitPrice * OD.Quantity) * (1 - OD.Discount)) AS TotalSpent
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY TotalSpent DESC;
GO


SELECT 
    P.ProductID, 
    P.ProductName, 
    SUM(OD.Quantity) AS TotalSold
FROM Products P
JOIN OrderDetails OD ON P.ProductID = OD.ProductID
GROUP BY P.ProductID, P.ProductName
ORDER BY TotalSold DESC;
GO


SELECT 
    YEAR(O.OrderDate) AS OrderYear, 
    MONTH(O.OrderDate) AS OrderMonth,
    C.CategoryName,
    SUM((OD.UnitPrice * OD.Quantity) * (1 - OD.Discount)) AS MonthlyRevenue
FROM Orders O
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
JOIN Categories C ON P.CategoryID = C.CategoryID
GROUP BY YEAR(O.OrderDate), MONTH(O.OrderDate), C.CategoryName
ORDER BY OrderYear, OrderMonth, C.CategoryName;
GO


