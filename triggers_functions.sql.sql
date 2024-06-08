-- פונקציה לחישוב הנחה
CREATE FUNCTION CalculateDiscount(@OrderID INT)
RETURNS DECIMAL(18, 2)
AS
BEGIN
    DECLARE @Total DECIMAL(18, 2)
    SELECT @Total = SUM((UnitPrice * Quantity) * (1 - Discount))
    FROM OrderDetails
    WHERE OrderID = @OrderID

    RETURN @Total
END;
GO

-- טריגר לעדכון מלאי אחרי כל הוספה להזמנה
CREATE TRIGGER UpdateStockAfterOrder
ON OrderDetails
AFTER INSERT
AS
BEGIN
    DECLARE @ProductID INT, @Quantity INT

    SELECT @ProductID = INSERTED.ProductID, @Quantity = INSERTED.Quantity
    FROM INSERTED

    UPDATE Products
    SET UnitsInStock = UnitsInStock - @Quantity
    WHERE ProductID = @ProductID
END;
GO

-- פונקציה לחישוב מספר ההזמנות של לקוח
CREATE FUNCTION GetCustomerOrderCount(@CustomerID INT)
RETURNS INT
AS
BEGIN
    DECLARE @OrderCount INT
    SELECT @OrderCount = COUNT(*)
    FROM Orders
    WHERE CustomerID = @CustomerID

    RETURN @OrderCount
END;
GO

-- פונקציה לחישוב הסכום הכולל של הזמנה
CREATE FUNCTION GetOrderTotal(@OrderID INT)
RETURNS DECIMAL(18, 2)
AS
BEGIN
    DECLARE @Total DECIMAL(18, 2)
    SELECT @Total = SUM((UnitPrice * Quantity) * (1 - Discount))
    FROM OrderDetails
    WHERE OrderID = @OrderID

    RETURN @Total
END;
GO


-- טריגר לעדכון מספר ההזמנות של לקוח לאחר הוספת הזמנה חדשה
CREATE TRIGGER UpdateCustomerOrderCountAfterInsert
ON Orders
AFTER INSERT
AS
BEGIN
    DECLARE @CustomerID INT

    SELECT @CustomerID = INSERTED.CustomerID
    FROM INSERTED

    UPDATE Customers
    SET OrderCount = dbo.GetCustomerOrderCount(@CustomerID)
    WHERE CustomerID = @CustomerID
END;
GO


-- טריגר לעדכון מצב מלאי המוצר לאחר עדכון פרטי הזמנה
CREATE TRIGGER UpdateStockAfterOrderUpdate
ON OrderDetails
AFTER UPDATE
AS
BEGIN
    DECLARE @ProductID INT, @OldQuantity INT, @NewQuantity INT

    SELECT @ProductID = INSERTED.ProductID, @NewQuantity = INSERTED.Quantity
    FROM INSERTED

    SELECT @OldQuantity = DELETED.Quantity
    FROM DELETED

    UPDATE Products
    SET UnitsInStock = UnitsInStock + @OldQuantity - @NewQuantity
    WHERE ProductID = @ProductID
END;
GO
