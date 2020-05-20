name ='trung ran'
name1 = 'bap'
name2 = "bo"
name3 = 'mo'
name4 = 'mam tom'
name10= 'ca ran'
#list, array: dữ liệu kiểu danh sách, mảng. dữ liệu bthg kiểu int, string chỉ tạ ra lệnh print số hoặc chữ. nhg dữ liệu list có thể in được cả 2.
mon_an = ['trung ran','bap','mo','bo','mam tom'] #buoc khoi tao(i: initialize)
print(mon_an)

#mon_an[1,2,3]: 1,2,3 goi la phan tu(value), ngam se theo thu tu la 0,1,2 goi la index, -1,-2,-3 la index chay nguoc lai

# buoc:READ
mon_an = ['trung ran','bap','mo','bo','mam tom']
print(mon_an[0])  #Read: trung ran
print(mon_an[-1])  #Read: mam tom
#print(mon_an[value1],mon_an[value2]): in ra 2 mon

mon_an = ['trung ran','bap','mo','bo','mam tom','thit cho']
for i in range(5): #co 5 phan tu
    print(mon_an[i])


print(len(mon_an))    #in ra theo do dai
for i in range(len(mon_an)):
    print(mon_an[i])

for value in mon_an: #giong dong tren, giam chu
    print(value)

for value in ['trung ran','bap','mo','bo','mam tom']:
    print(value)


mon_an = ['trung ran','bap','mo','bo','mam tom']
mon_an.append('sushi') #them vao cuoi de dam bao thu tu k bi xao tron
print(mon_an)

#lenh Creat
name10=input()
mon_an.append(name10) #them mon an theo input

#lenh update
mon_an[0] = 'bach tuoc' #update
print(mon_an)

#lenh delete
deleted_item = mon_an.pop() #khong dien so no se xoa mon cuoi cung
print(mon_an)
print(deleted_item)