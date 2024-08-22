from database_connection import create_connection

# פונקציה להוספת מוצר חדש
def add_product(product_name, category, quantity):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ProductID, Quantity FROM Products 
        WHERE ProductName = ? AND Category = ?
    """, (product_name, category))
    existing_product = cursor.fetchone()
    
    if existing_product:
        product_id, existing_quantity = existing_product
        new_quantity = existing_quantity + quantity
        cursor.execute("""
            UPDATE Products 
            SET Quantity = ? 
            WHERE ProductID = ?
        """, (new_quantity, product_id))
        conn.commit()
        print(f"Product '{product_name}' updated. New quantity: {new_quantity}")
    else:
        cursor.execute("""
            INSERT INTO Products (ProductName, Category, Quantity)
            VALUES (?, ?, ?)
        """, (product_name, category, quantity))
        conn.commit()
        
        # חיפוש ה-ProductID של המוצר שהתווסף
        cursor.execute("""
            SELECT ProductID FROM Products 
            WHERE ProductName = ? AND Category = ?
        """, (product_name, category))
        product_id = cursor.fetchone()[0]
        print(f"Product '{product_name}' added with quantity: {quantity}")

    # הוספת רשומה לטבלת ההיסטוריה
    cursor.execute("""
        INSERT INTO ProductHistory (ProductID, ProductName, Category, Quantity)
        VALUES (?, ?, ?, ?)
    """, (product_id, product_name, category, quantity))
    conn.commit()

    conn.close()
    return product_id


# פונקציה לצפייה בכל המוצרים
def view_products():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return rows


def view_product_history():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ProductHistory ORDER BY AddedDate DESC")
    rows = cursor.fetchall()
    conn.close()
    
    print("--- Product History ---")
    for record in rows:
        print(f"History ID: {record[0]}, Product ID: {record[1]}, Product Name: {record[2]}, Category: {record[3]}, Quantity: {record[4]}, Added Date: {record[5]}")
    
    return rows


# מחיקת כל המוצרים
def delete_all_products():
    conn = create_connection()
    cursor = conn.cursor()
    
    # מחיקת כל הנתונים בטבלת ProductHistory
    cursor.execute("DELETE FROM ProductHistory")
    conn.commit()

    # מחיקת כל הנתונים בטבלת Products
    cursor.execute("DELETE FROM Products")
    conn.commit()
    
    conn.close()
    print("All products and related history have been deleted.")


# מחיקת כל ההיסטוריה
def delete_product_history():
    conn = create_connection()
    cursor = conn.cursor()
    
    # מחיקת כל הנתונים בטבלת ProductHistory
    cursor.execute("DELETE FROM ProductHistory")
    conn.commit()
    
    conn.close()
    print("All product history has been deleted.")


def delete_product(product_id):
    conn = create_connection()
    cursor = conn.cursor()

    # מחיקת רשומות תלויות בטבלת ProductHistory
    cursor.execute("DELETE FROM ProductHistory WHERE ProductID = ?", (product_id,))
    conn.commit()

    # מחיקת המוצר מטבלת Products
    cursor.execute("DELETE FROM Products WHERE ProductID = ?", (product_id,))
    conn.commit()

    conn.close()
    print(f"Product ID: {product_id} deleted successfully.")
