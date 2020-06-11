import pymysql #ket noi vao mysql 

client = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '0804'
)

cursor = client.cursor()                      #con tro? nhu con chuot 

# cursor.execute('CREATE DATABASE d4e12')       #chay sql, tao folder vao bang mysql  -> schema -> an refresh

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS d4e12.cake (
  name VARCHAR(255) PRIMARY KEY, 
  calor_rate INT(11)
)
'''
)

cursor.execute( 
    '''
    CREATE TABLE IF NOT EXISTS d4e12.ingredient (
        name VARCHAR(255) PRIMARY KEY,
        cake_name VARCHAR(255) UNIQUE REFERENCES d4e12.cake(name) 
    )
    '''
)

cake_name = 'otga'
cursor.execute(
    f'''
        INSERT INTO d4e12.cake(name, calor_rate)
        VALUES ('{cake_name}',3000),('agto',6000)
    '''
)


client.commit()