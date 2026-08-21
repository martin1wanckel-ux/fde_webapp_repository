import sqlite3


def initialize_fde_db()-> None:
    conn = sqlite3.connect("fde_lab.db")
    cursor = conn.cursor()

    # create users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    # create orders
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    # Create an INDEX for user_id in Orders
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id)
    """)
    conn.commit()
    conn.close()

def add_entries()-> None:
    conn = sqlite3.connect("fde_lab.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)" , ("Alice",)) # Insert Alice
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",)) # Insert Bob
    cursor.execute("INSERT INTO orders (user_id, amount) VALUES (?,?)", (1,30)) # first order alice
    cursor.execute("INSERT INTO orders (user_id, amount) VALUES (?,?)", (1,50)) # second order alice , no explicit order for BOB
    conn.commit()
    conn.close()


if __name__ == "__main__":
    initialize_fde_db()
    add_entries()