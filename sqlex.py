import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
restaurants_db = mongo_client.get_database('mysql_ex')
restaurants_collection = restaurants_db.get_collection('restaurants')

mysql_client = pymysql.connect(
    host='localhost',
    user='root',
    password='0804',
#     # cursorclass = pymysql.cursor.DictCursor


cursor = mysql_client.cursor()

cursor.execute('CREATE DATABASE mysql_ex')

cursor.execute (
    '''
    CREATE TABLE IF NOT EXISTS mysql_ex.restaurants(
        _id VARCHAR (255) PRIMARY KEY,
        building VARCHAR(255),
        zipcode VARCHAR(255),
        street VARCHAR(255),
        borough VARCHAR(255),
        cuisine VARCHAR(255)

    )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS mysql_ex.grade(
        _id INT(11) PRIMARY KEY,
        restaurant_id VARCHAR(255) REFERENCES mysql_ex.restaurant(id),
        grade VARCHAR(45),
        score VARCHAR(45)
    )
    '''
)

query = {
    'building':{'$ne':None},
    'zipcode':{'$ne':None},
    'street':{'$ne':None},
    'borough':{'$ne':None},
    'cuisine':{'$ne':None}
}

for restaurant in restaurants_collection.find(query):
    print(restaurant)
    restaurant_id = str(restaurants['_id'])
    cursor.execute(
        f'''
        INSERT INTO mysql_ex.restaurants(_id, building, zipcode, street, borough, cuisine)
        VALUES('{'restaurant_id'},
        '{restaurants['address']['building']}',
        '{restaurants['address']['coord'][1]},
        '{restaurants['address']['coord'][0]},
        '{restaurants['borough']},
        '{restaurants['cuisine']}
        )

        '''
        
    )


mysql_client.commit()

