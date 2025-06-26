
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',              
        database='python_data'
    )

def create_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            category VARCHAR(255),
            amount FLOAT,
            description TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_expense(date, category, amount, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, category, amount, description)
        VALUES (%s, %s, %s, %s)
    """, (date, category, amount, description))
    conn.commit()
    cursor.close()
    conn.close()
    print("Expense added successfully!")

def view_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, category, amount, description FROM expenses")
    rows = cursor.fetchall()
    print(f"\n {'Date':<12} {'Category':<15} {'Amount':<10} Description")
    print("-" * 50)
    for row in rows:
        print(f" {str(row[0]):<12} {row[1]:<15} ₹{row[2]:<10} {row[3]}")
    print()
    cursor.close()
    conn.close()

def total_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0] or 0
    print(f"\n Total Spent: ₹{total:.2f}\n")
    cursor.close()
    conn.close()

def expenses_by_category():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    print("\n Spending by Category:")
    for row in rows:
        print(f"  {row[0]}: ₹{row[1]:.2f}")
    print()
    cursor.close()
    conn.close()

def menu():
    create_table_if_not_exists()
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")
        if choice == '1':
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category (Food, Travel, Bills...): ")
            amount = float(input("Amount: ₹"))
            description = input("Description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            expenses_by_category()
        elif choice == '5':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Try again!\n")

if __name__ == '__main__':
    menu()
