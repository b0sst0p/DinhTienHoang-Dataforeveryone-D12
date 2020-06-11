person = ['Duc',96,'Son la', 1, False]
dictionary_person = {
    'name': 'Duc',                  #key : value, (cach nhau 1 dau phay) (value co the la list, value, dictionary khac)
    'YOB': 96,
    'home_town':'Son La'
}

# I C R U D
#Read
# print('name' in dictionary_person)
if 'name' in dictionary_person: #check if key in a dictionary
    print(dictionary_person['name']) #Read #access key 'name'

#C
dictionary_person['rela_status'] =  False #CREAT
dictionary_person['name'] = 'not Duc'
print(dictionary_person)

#D
del dictionary_person['name']
print(dictionary_person)

#duyet theo key
for key in dictionary_person:
    print(key) #in key
    print(key, dictionary_person[key]) # in cho dep