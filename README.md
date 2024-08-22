# Order Inventory Management System

This project is an Order Inventory Management System built using Python, SQL, and Flask. It is designed to manage product inventory and customer orders in a store, with separate dashboards for store managers and customers.

## Features

### For Customers:
- **Registration and Login**: Customers can register with a username and password, which will be used as their customer name for orders.
- **Place Orders**: Customers can place orders by selecting a product by its name and specifying the quantity.
- **Order Status**: After placing an order, customers receive an order number and can check the status of their order (e.g., Received, In Process, On the Way, Delivered).
- **Search Products**: Customers can search for products by name or view the available quantity in the store.
- **View Order**: Customers can only view their own orders by entering their order number.

### For Store Managers:
- **Manager Login**: Managers can log in with a secure password (e.g., `gal24`).
- **Manage Products**: Managers can add new products to the inventory, specifying the product category, name, and initial stock quantity.
- **View All Products**: Managers can view all products in the store, sorted by category or other criteria.
- **Approve Orders**: Managers can view customer orders, approve them, and update the order status as it progresses through different stages.
- **Delete Products**: Managers can delete products from the inventory.

## Project Structure

SQLOrderInventorySystem/
│
├── SQL Server Scripts1/
│ ├── create_tables.sql
│ ├── insert_data.sql
│ ├── queries.sql
│ ├── triggers_functions.sql
│
├── templates/
│ ├── customer_dashboard.html
│ ├── index.html
│ ├── login.html
│ ├── manager_dashboard.html
│ ├── order_status.html
│ └── product_search.html
│
├── app.py
├── database_connection.py
├── order_management.py
├── product_management.py
└── test_product_management.py


- **SQL Server Scripts1/**: Contains the SQL scripts for creating tables, inserting data, running queries, and triggers/functions.
- **templates/**: HTML templates for the web application, including dashboards for customers and managers, and pages for login and product search.
- **app.py**: The main Flask application that handles routing and logic for the web interface.
- **database_connection.py**: Handles the connection to the SQL Server database.
- **order_management.py**: Contains functions for managing customer orders.
- **product_management.py**: Contains functions for managing products in the inventory.
- **test_product_management.py**: A test script for testing product management functionality.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TomerDahari/Order-Inventory-Management-System.git
2. **Navigate to the project directory**:
   ```bash
   cd Order-Inventory-Management-System
Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

Install dependencies:
pip install -r requirements.txt

Set up the database:
Run the SQL scripts in the SQL Server Scripts1/ directory to set up the database, insert initial data, and create necessary triggers and functions.

Run the application:
flask run

Access the application:
Open your browser and go to http://127.0.0.1:5000 to access the Order Inventory Management System.
