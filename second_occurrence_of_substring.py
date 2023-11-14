#given a string and a substring, look for the second substring. If there is not a second substring, break and say there is no second occurence
#if there is the substring, remove that first character and search the string again, if there is, then print out that index + 1 given we removed the first character of the first occurance, if there isnt, then do as above
string = input('Please type in a string: ')
sub_string = input('Please type in a substring: ')
index = string.find(sub_string)

while True:
    if index:
        if index ==0:
            string = string[0 + len(sub_string)-1:]
            new_index = string.find(sub_string)
            if new_index ==0:
                print(f'The second occurrence of the substring is at index {new_index + len(sub_string)+1}.')
                break
            elif new_index !=0:
                print(f'The second occurrence of the substring is at index {new_index + len(sub_string)}.')
                break
            else:
                print('The substring does not occur twice in the string.')
                break
                
        elif index !=0:
            string = string[0:index] + string[index+len(sub_string)+1]
            new_index = string.find(sub_string)
            if new_index ==0:
                print(f'The second occurrence of the substring is at index {new_index + len(sub_string)+1}.')
                break
            elif new_index !=0:
                print(f'The second occurrence of the substring is at index {new_index + len(sub_string)}.')
                break
            else:
                print('The substring does not occur twice in the string.')
                break
        
    

        
            
