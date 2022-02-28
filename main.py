import sys
from DTO import *
from Repository import repo


def main(args):
    repo.init()
    repo.create_tables()
    repo._commit()
    file = open('config.txt')
    file.readline()
    for line in file:
        line = line.split("\n")[0]
        if len(line.split(",")) == 4:
            hat_id = line.split(',')[0]
            topping = line.split(',')[1]
            supplier_id = line.split(',')[2]
            quantity = line.split(',')[3]
            toInsert = Hat(hat_id, topping, supplier_id, quantity)
            repo.hats.insert(toInsert)
        else:
            supplier_id = line.split(',')[0]
            supplier_Name = line.split(',')[1]
            toInsert = Supplier(supplier_id, supplier_Name)
            repo.suppliers.insert(toInsert)
    file = open('orders.txt')
    orderID = 1
    output = open('output.txt', 'w')
    for line in file:
        line = line.split("\n")[0]
        location = line.split(',')[0]
        topping = line.split(',')[1]
        hatToOrder = repo.hats.find(topping)
        supplier = repo.suppliers.find(hatToOrder.supplier).name
        orderToInsert = Order(orderID, location, hatToOrder.id)
        repo.orders.insert(orderToInsert)
        orderID += 1
        output.write(topping + "," + supplier + "," + location + "\n")
        if hatToOrder.quantity > 0:
            repo.hats.updateQuantity(hatToOrder.id, hatToOrder.quantity-1)
        if hatToOrder.quantity-1 == 0:
            repo.hats.removeByQuantity(hatToOrder.id)
    output.close()
    repo._close() 
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)
