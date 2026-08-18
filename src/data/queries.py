import sqlite3 

def get_user_totals(min_amonunt = 0) -> list[tuple]:
    conn = sqlite3.connect('fde_lab.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.name , users.id as user_id, COALESCE(SUM(amount), 0.0) AS total_orders 
        FROM users
        LEFT JOIN orders
        ON users.id = orders.user_id 
        GROUP BY user_id, users.name
        HAVING COALESCE(SUM(amount) , 0)  >= (?);""", (min_amonunt,))
    results = cursor.fetchall()
    conn.close()
    return results # a l
# FROM → JOIN → WHERE → GROUP BY → HAVING. Immer in dieser Reihenfolge
def get_specific_user_total(user_id : int, min_amount : int = 0): # parameter mit default hinter parameter ohne
    conn = sqlite3.connect('fde_lab.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT users.name , users.id as user_id, COALESCE(SUM(amount), 0.0) AS total_orders 
        FROM users
        LEFT JOIN orders
        ON users.id = orders.user_id 
        WHERE users.id = (?)
        GROUP BY user_id, users.name
        HAVING COALESCE(SUM(amount) , 0)  >= (?)
        ORDER BY total_orders;""", (user_id ,min_amount))

    results = cursor.fetchall()
    conn.close()
    return results
        



if __name__ == "__main__":
    results = get_user_totals()
    print("With 0 as minimum amount:" , results)
    results = get_user_totals(50)
    print("With 50 as minimum amount:" , results)
    results = get_specific_user_total( user_id= 1 , min_amount= 0 )
    print("Specific user Query:", results)
