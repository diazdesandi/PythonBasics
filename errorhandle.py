# Catchihg runtime errors
x = 42
y = 2
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')

