#cho nguoi dung chon 1 trong so cac mon an va sua thanh mon ho muon
mon_an = ['trung ran', 'ca','thit lon','thit bo','trung luoc']
for i in range(len(mon_an)):
    print(i+1, mon_an[i])

#cach 2: de ro index va value
for index, value in enumerate (mon_an):
    print(index+1, value)


#bai day du index > mon
index = int(input("enter the number you want to edit:"))
value = input('new value:')
mon_an[index-1] = value
for index, value in enumerate (mon_an):
    print(index+1, value)

#sua mon truc tiep mon => mon
old_value = input("enter the number you want to edit:")
value = input('new value:')
index1= mon_an.index(old_value)
mon_an[index1] = value
for index1, value in enumerate (mon_an):
    print(index1+1, value)