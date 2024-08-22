import pyodbc

def create_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-MHPNLKG;'  # שם השרת שלך
        'DATABASE=master;'  # שם בסיס הנתונים שלך
        'Trusted_Connection=yes;'
    )
    return conn

# דוגמה לחיבור וניתוק
conn = create_connection()
print("Connection successful!")
conn.close()
