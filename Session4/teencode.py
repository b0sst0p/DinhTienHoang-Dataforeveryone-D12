dictionary_teencode ={
    'vk':'vu khi',
    'hg':'ha giang',
    'sp':'sapa'
}

for a in dictionary_teencode:
    print(a, end='')
your_code = input('your code:')

if your_code in dictionary_teencode:
    print('tran:', dictionary_teencode[your_code])
else:
    print('not found, do you want to contribute this word:(y/n):')
    answer = input()
    a = y
    b = n
    if answer == a:
        dictionary_teencode.update({''})
        print('update')
        print(*dictionary_teencode)
        

    