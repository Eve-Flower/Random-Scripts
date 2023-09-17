#fizzbuzz
#get the user number using input
#establish counter and then while loop that prints current number and increments by 1
#if the number is a multiple of 3 and 5 print fizzbuzz
#make an else if, that checks if the number is a multiple of 3, then fizz if true
#make an else if, that checks if the number is a multiple of 5, then buzz if true

number = int(input('enter your number to get fizzin: '))

counter = 1

while counter <= number:
    if counter % 3 == 0 and counter % 5 == 0:
        print(f'{counter} says fizzbuzz')
        counter += 1
    elif counter % 3 == 0:
        print(f'{counter} says fizz')
        counter += 1
    elif counter % 5 == 0:
        print(f'{counter} says buzz')
        counter += 1
    else:
        print(f'{counter} says nothing tbh')
        counter += 1

