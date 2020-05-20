flock = [5,7,300,90,24,50,75]
print('Hello my name is Hiep and these are my sheep size:')
print(*flock)


biggest_size = max(flock)
print('Now my biggest sheep has size', biggest_size, 'let shear it')

x = flock.index(biggest_size)
flock[x]= 8
print('after shearing','here is my flock')
print(*flock)


A = 50
new_flock = [b + A for b in flock]
print('One month has passed','now here is my flock')
print(new_flock)

for i in range(4):
    print( i+1,'month has passed','now here is my flock')
    new_flock1 =[b+50 for b in flock]
    print(new_flock1)
    b_size = max(new_flock1)
    print('Now my biggest sheep has size', b_size, 'let shear it')
    y = new_flock1.index(b_size)
    new_flock1[y] = 8
    print('after shearing here is my flock')
    print(*new_flock1)
    
    

print('My flock has size in total:',sum(new_flock1))
print('I would get',sum(new_flock1), '*',2, '=', sum(new_flock1)*2)