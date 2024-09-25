# pharmacy_manager.py (business logic for Pharmacy Manager)
from database import Database

class PharmacyManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = Database()

    def register(self):
        query = "INSERT INTO managers (username, password) VALUES (%s, %s)"
        self.db.execute_query(query, (self.username, self.password))

    def login(self):
        query = "SELECT * FROM managers WHERE username = %s AND password = %s"
        result = self.db.fetch_all(query, (self.username, self.password))
        if result:
            return True
        else:
            return False

    def add_medicine(self, medicine_name, qty, added_date, price):
        query = "INSERT INTO medicines (medicine_name, qty, added_date, price) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (medicine_name, qty, added_date, price))

    def view_medicines(self):
        query = "SELECT * FROM medicines"
        return self.db.fetch_all(query)

    def delete_medicine(self, medicine_id):
        query = "DELETE FROM medicines WHERE id = %s"
        self.db.execute_query(query, (medicine_id,))

class Medicine:
    def __init__(self, medicine_name, qty, added_date, price):
        self.medicine_name = medicine_name
        self._qty = qty
        self.added_date = added_date
        self.price = price

    def get_qty(self):
        return self._qty

    def set_qty(self, qty):
        self._qty = qty