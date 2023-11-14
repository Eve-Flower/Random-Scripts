index = 0
string = input('Please type in a string: ')
while index != len(string):
    print(string[-(index+1):])
    index+=1