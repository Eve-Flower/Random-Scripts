string = input('Word: ')
print('*'*30)
if len(string) % 2 == 0:
    print('*' + ' '*(int((30-len(string)-2)/2))+ string + ' '*(int((30-len(string)-2)/2))+ '*')
else:
    print('*' + ' '*(int((30-len(string)-1)/2))+ string + ' '*(int((30-len((string )-2)/2))+ '*'))

print('*'*30)