from flask import Flask, render_template, request, redirect, url_for, flash, session
from database_connection import create_connection
from product_management import add_product, view_products, delete_product
from order_management import place_order, update_order_status, view_orders


app = Flask(__name__)

app.secret_key = 'your_secret_key'  # מפתח סודי עבור הודעות flash

# דף הבית - כניסה כלקוח או כמנהל
@app.route('/')
def index():
    return render_template('index.html')

# דף כניסה ללקוח או מנהל
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        if role == 'manager':
            password = request.form['password']
            if password == 'gal24':
                return redirect(url_for('manager_dashboard'))
            else:
                flash('Incorrect password. Please try again.')
                return redirect(url_for('login'))
        elif role == 'customer':
            return redirect(url_for('customer_dashboard'))
    return render_template('login.html')

# דף לקוח - לבצע הזמנה, לבדוק זמינות פריט, לראות סטטוס הזמנה
@app.route('/customer_dashboard', methods=['GET', 'POST'])
def customer_dashboard():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        place_order(customer_name, product_id, int(quantity))
        return redirect(url_for('order_status', customer_name=customer_name))
    return render_template('customer_dashboard.html')


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product_route(product_id):
    delete_product(product_id)
    return redirect(url_for('manager_dashboard'))


# דף מנהל - הוספה וניהול של מוצרים והזמנות
@app.route('/manager_dashboard', methods=['GET', 'POST'])
def manager_dashboard():
    if request.method == 'POST':
        if 'add_product' in request.form:
            product_name = request.form['product_name']
            category = request.form['category']
            quantity = request.form['quantity']
            add_product(product_name, category, int(quantity))
        elif 'update_order' in request.form:
            order_id = request.form['order_id']
            new_status = request.form['new_status']
            update_order_status(int(order_id), new_status)
        return redirect(url_for('manager_dashboard'))
    products = view_products()
    orders = view_orders()
    return render_template('manager_dashboard.html', products=products, orders=orders)

# דף צפייה בסטטוס הזמנה ללקוח
@app.route('/order_status/<customer_name>')
def order_status(customer_name):
    orders = view_orders()
    return render_template('order_status.html', orders=orders, customer_name=customer_name)

# דף חיפוש מוצר עבור לקוח
@app.route('/product_search', methods=['GET', 'POST'])
def product_search():
    products = []
    if request.method == 'POST':
        search_term = request.form['search_term']
        products = [product for product in view_products() if search_term.lower() in product[1].lower()]
    return render_template('product_search.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)

app.secret_key = 'your_secret_key'  # מפתח סודי עבור session

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = create_connection()
        cursor = conn.cursor()
        
        # בדיקה אם שם המשתמש כבר קיים
        cursor.execute("SELECT * FROM Customers WHERE Username = ?", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash('Username already exists. Please choose a different one.')
            return redirect(url_for('register'))
        
        # הוספת משתמש חדש
        cursor.execute("INSERT INTO Customers (Username, Password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        if role == 'manager':
            password = request.form['password']
            if password == 'gal24':
                session['role'] = 'manager'
                return redirect(url_for('manager_dashboard'))
            else:
                flash('Incorrect password. Please try again.')
                return redirect(url_for('login'))
        elif role == 'customer':
            username = request.form['username']
            password = request.form['password']
            
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customers WHERE Username = ? AND Password = ?", (username, password))
            user = cursor.fetchone()
            conn.close()
            
            if user:
                session['username'] = username
                return redirect(url_for('customer_dashboard'))
            else:
                flash('Incorrect username or password. Please try again.')
                return redirect(url_for('login'))
    
    return render_template('login.html')


@app.route('/customer_dashboard', methods=['GET', 'POST'])
def customer_dashboard():
    if 'username' not in session:
        flash('Please log in first.')
        return redirect(url_for('login'))

    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = request.form['quantity']

        # מציאת ה-ProductID לפי שם המוצר
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ProductID FROM Products WHERE ProductName = ?", (product_name,))
        product = cursor.fetchone()

        if product:
            product_id = product[0]
            order_id = place_order(session['username'], product_id, int(quantity))
            flash(f'Order placed successfully! Order ID: {order_id}')
        else:
            flash('Product not found. Please try again.')

        conn.close()
    
    return render_template('customer_dashboard.html')


@app.route('/order_status', methods=['GET', 'POST'])
def order_status():
    if 'username' not in session:
        flash('Please log in first.')
        return redirect(url_for('login'))

    orders = []
    if request.method == 'POST':
        order_id = request.form['order_id']
        
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT o.OrderID, o.CustomerName, o.OrderDate, s.StatusName, o.ProductID, o.Quantity
            FROM Orders o
            JOIN OrderStatus s ON o.StatusID = s.StatusID
            WHERE o.CustomerName = ? AND o.OrderID = ?
        """, (session['username'], order_id))
        orders = cursor.fetchall()
        conn.close()
    
    return render_template('order_status.html', orders=orders)
