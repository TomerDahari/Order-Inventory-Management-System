# ייבוא הפונקציה ליצירת חיבור לבסיס הנתונים
from database_connection import create_connection

# פונקציה לביצוע הזמנה חדשה
def place_order(customer_name, product_id, quantity):
    conn = create_connection()
    cursor = conn.cursor()

    # יצירת הזמנה חדשה עם סטטוס התחלתי "Pending" והחזרת ה-OrderID שנוצר
    cursor.execute("""
        INSERT INTO Orders (CustomerName, OrderDate, OrderStatus, ProductID, Quantity)
        OUTPUT INSERTED.OrderID
        VALUES (?, GETDATE(), 'Pending', ?, ?)
    """, (customer_name, product_id, quantity))
    
    order_id = cursor.fetchone()[0]
    
    conn.commit()
    conn.close()
    
    print(f"Order placed successfully! Order ID: {order_id}")
    return order_id


# פונקציה לעדכון סטטוס הזמנה
def update_order_status(order_id, new_status):
    conn = create_connection()
    cursor = conn.cursor()
    
    # עדכון הסטטוס של ההזמנה
    cursor.execute("""
        UPDATE Orders
        SET StatusID = (SELECT StatusID FROM OrderStatus WHERE StatusName = ?)
        WHERE OrderID = ?
    """, (new_status, order_id))
    conn.commit()
    conn.close()
    print(f"Order ID: {order_id} updated to status: {new_status}")

# פונקציה לצפייה בכל ההזמנות והסטטוסים
def view_orders():
    conn = create_connection()
    cursor = conn.cursor()
    
    # שליפת כל ההזמנות והסטטוסים
    cursor.execute("""
        SELECT o.OrderID, o.CustomerName, o.OrderDate, s.StatusName, o.ProductID, o.Quantity
        FROM Orders o
        JOIN OrderStatus s ON o.StatusID = s.StatusID
        ORDER BY o.OrderDate DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    
    print("--- All Orders ---")
    for row in rows:
        print(f"Order ID: {row[0]}, Customer: {row[1]}, Date: {row[2]}, Status: {row[3]}, Product ID: {row[4]}, Quantity: {row[5]}")
    
    return rows
