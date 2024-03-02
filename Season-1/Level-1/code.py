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
    net_payment = 0
    total_payable = 0
    total_receivable = 0

    for item in order.items:
        if item.type == 'payment':
            net_payment += item.amount
        elif item.type == 'product':
            total_payable += item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    total_receivable = total_payable - net_payment

    if total_receivable != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, total_receivable)
    else:
        return "Order ID: %s - Full payment received!" % order.id
