'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    if not isinstance(order.items, list) or not all(isinstance(item, Item) for item in order.items):
        return "Invalid order items"

    net = 0
    invalid_items = []

    for item in order.items:
        if item.type == 'payment':
            net += item.amount
        elif item.type == 'product':
            net -= item.amount * item.quantity
        else:
            invalid_items.append(item.type)

    if invalid_items:
        return "Invalid item types: %s" % ', '.join(invalid_items)

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
