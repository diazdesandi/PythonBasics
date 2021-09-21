price = 12

# Print tax inside if - else
if price >= 1.00:
    tax = 0.7
    print(tax)
else:
    tax = 0
    print(tax)

# Print tax after if - else
if price >= 1.00:
    tax = 0.7
else:
    tax = 0
print(tax)

# String comparing
# String comparsions are case sensitive

country = 'CANADA'
if country == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')

# Fixed
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')