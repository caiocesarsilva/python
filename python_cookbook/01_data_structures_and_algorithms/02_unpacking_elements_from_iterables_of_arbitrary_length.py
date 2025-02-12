#You need to unpack N elements from a iterable, but the iterable may be longer than N elements, causing a "too many values to unpack" exception.
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)