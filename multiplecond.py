if country == 'Canada':
#if province == 'Alberta' or province == 'Nunavut':
# Using IN operator
    if province in('Alberta','Nunavut','Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else: #Acts as default condition
        tax = 0.15

else:
    tax == 0.0