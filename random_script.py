#now lets make an if statement to print what the user has said

evens = []
odds = []

def sort_numbers_up_to(number):
    evens = [number for number in range(number+1) if number % 2 == 0]
    odds = [number for number in range(number+1) if number % 2 != 0]
    print(f'this is number: {number}')
    print(f'this is evens: {evens}')
    print(f'this is odds: {odds}')
    
sort_numbers_up_to(102)
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [x for sublist in nested_list for x in sublist]
print(flattened)
#unflatten = [[x] for x in flattened if x != x in nested_list]
#print(unflatten)

x = 2 + 3
print('2 + 3 = {}'.format(x))