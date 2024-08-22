from order_management import place_order, update_order_status, view_orders
from product_management import add_product

if __name__ == "__main__":
    # הוספת מוצר לדוגמה
    product_id = add_product("Laptop", "Electronics", 10)

    # ביצוע הזמנה חדשה
    order_id = place_order("John Doe", product_id, 2)

    # צפייה בכל ההזמנות
    view_orders()

    # עדכון סטטוס ההזמנה ל-"In Process"
    update_order_status(order_id, "In Process")

    # צפייה מחדש בהזמנות עם הסטטוס החדש
    view_orders()
