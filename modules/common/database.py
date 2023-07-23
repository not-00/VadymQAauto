import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/vadymkuzmich/VadymQAauto' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(sefl):
        sqlite_select_Query = "SELECT sqlite_version();"
        sefl.cursor.execute(sqlite_select_Query)
        record = sefl.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()
        
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_products_where_qnt_more_that_entered(self, qnt):
        query = f"SELECT name, quantity FROM products WHERE quantity > {qnt}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_user(self, user_id, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES ({user_id}, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def get_users_where_names_stars_with(self, first_letter):
        query = f"SELECT id, name, country FROM customers WHERE name LIKE '{first_letter}%'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def select_product(self, product_id):
        query = f"SELECT * FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product_without_desc(self, product_id, name, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                VALUES ({product_id}, '{name}', null,{qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_user_where_id_is_null(self, name, address, city, postalCode, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
            VALUES (null, '{name}', '{address}', '{city}', '{postalCode}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()