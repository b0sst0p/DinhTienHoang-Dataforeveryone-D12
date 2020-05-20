# list trong cua hang
# 4 lua chon c,r, u,d
#C them cai gi 
#R in ra toan bo item
#U: sua gi? thanh gi?
#D: xoa item nao?
#Them bn lan cung dc
#elif: dung chay mai
stores = ['ca sau','khung long','phi thuyen']
while True:
    choices = input('what you want to do? (C R U D) ')
    if choices == 'c':
        new_item = input('what you want to add: ')
        stores.append(new_item)
        print(*stores)
    elif choices == 'r':
        print(*stores)
    elif choices == 'u':
        for index, value in enumerate(stores):
            print(index+1,value)
        update_index = int(input('enter the position u want to make change: '))
        update_value = input('enter new value: ')
        stores[update_index-1] = update_value
        print(*stores)
    elif choices == 'd':
        for index, value in enumerate(stores):
            print(index+1,value)
        delete_index = int(input('enter the position u want to delete: '))
        stores.pop(delete_index-1)
        print(*stores)
    else:
        break

