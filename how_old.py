from datetime import date

today = date.today()
user_name = input('What is your name? ')
user_birth_year = int(input('What year were you born? '))
user_birth_month = int(input('What month were you born? '))
user_birth_day = int(input('What day were you born? '))

total_days_alive = ((today.day - user_birth_day) + ((((today.year)-(user_birth_year))*365)+((today.month - user_birth_month)*30)))
print(f'hi {user_name}, have survived for about {total_days_alive} days and are {total_days_alive/365} years old!')
print(today.day)
print(today.month)
print(today.year)