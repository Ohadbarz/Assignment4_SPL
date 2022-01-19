import atexit
import sqlite3
from DAO import _Hats, _Suppliers, _Orders


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('myDataBase.db')
        self.hats = _Hats(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.orders = _Orders(self._conn)

    def init(self):
        self.__init__()

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def _commit(self):
        self._conn.commit()


    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE IF NOT EXISTS Hats (
            id        INT          PRIMARY KEY,
            topping   STRING       NOT NULL,
            supplier  INT          references Supplier(id),
            quantity  INT          NOT NULL

    );

        CREATE TABLE IF NOT EXISTS Suppliers (
            id       INT       PRIMARY KEY,
            name     STRING    NOT NULL
    );

        CREATE TABLE IF NOT EXISTS Orders (
            id        INT        PRIMARY KEY ,
            location  STRING     NOT NULL,
            hat       INT        REFERENCES Hats(id)
    );
""")


repo = _Repository()
atexit.register(repo._close)