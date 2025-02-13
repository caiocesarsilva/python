#You need to unpack N elements from a iterable, but the iterable may be longer than N elements, causing a "too many values to unpack" exception.
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

######################################################################################################################################################

record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing, current = record
trailing_avg = sum(trailing) / len(trailing)
print('avg_comparison:',trailing_avg,',',current)

######################################################################################################################################################

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

######################################################################################################################################################

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

######################################################################################################################################################

data = ['ACME', 50, 91.1, (12, 18, 2012)]
name, *_, (*_, year) = data
print(name)
print(year)

######################################################################################################################################################

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

sum(items)