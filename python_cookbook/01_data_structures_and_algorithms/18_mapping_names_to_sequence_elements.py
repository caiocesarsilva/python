from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jones@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

#######################################################################

print(len(sub))
addr, joined = sub
print(addr)
print(joined)

#######################################################################

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def comput_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

#######################################################################

s = Stock('ACME', 100, 123.45)
print(s)
s = s._replace(shares=75)
print(s)

#######################################################################

from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price':123.45}
print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))