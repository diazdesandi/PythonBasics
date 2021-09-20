# Datetime library
from datetime import datetime

# Get current date
current_date = datetime.now()

# Print date
print('Today is:' + str(current_date))

# define period of time using timedelta
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was:' + str(yesterday))

# Request part of date
print('Day:' + str(current_date.day))
print('Month' + str(current_date.month))
print('Year:' + str(current_date.year))

# Birthday
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday' + str(birthday_date))

# Day before birthday
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))