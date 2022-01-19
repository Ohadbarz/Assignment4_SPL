# Data Access Objects:
# All of these are meant to be singletons
from DTO import Hat, Supplier, Order


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
               INSERT OR REPLACE INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def find(self, topping):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM Hats WHERE topping = ?
            ORDER BY supplier ASC
        """, [topping])
        toReturn = c.fetchone()
        if toReturn is None:
            None
        else:
            return Hat(*toReturn)

    def findByHat(self, hat):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM hats WHERE id = ?
        """, [hat])
        toReturn = c.fetchone
        if toReturn is None:
            None
        else:
            return Hat(*toReturn)

    def removeByQuantity(self, hat):
        c = self._conn.cursor()
        c.execute("""
                DELETE FROM hats WHERE id = ?
            """, [hat])

    def updateQuantity(self, hat,quantity):
        c = self._conn.cursor()
        c.execute("""
               UPDATE hats SET quantity = ? WHERE id = ?
            """, [quantity, hat])


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT OR REPLACE INTO suppliers (id, name) VALUES (?, ?)
        """, [supplier.id, supplier.name])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,name FROM suppliers WHERE id = ?
            """, [id])

        return Supplier(*c.fetchone())


class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
            INSERT OR REPLACE INTO orders (id, location, hat) VALUES (?, ?, ?)
        """, [order.id, order.location, order.hat])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, location, hat FROM orders
        """).fetchall()

        return [Order(*row) for row in all]

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,location,hat FROM suppliers WHERE id = ?
            """, [id])

        return Order(*c.fetchone())



