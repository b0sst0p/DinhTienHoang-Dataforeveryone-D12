import pymysql
from pymongo import MongoClient

mongo_client = MongoClient()
movie_db = mongo_client.get_database('d4e12')
movie_collection = movie_db.get_collection('movie')

mysql_client = pymysql.connect(
    host='localhost',
    user='root',
    password='0804',
    # cursorclass = pymysql.cursor.DictCursor
)

cursor = mysql_client.cursor()

# cursor.execute('CREATE DATABASE d4e12')

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS d4e12.movie (
        _id VARCHAR (255) PRIMARY KEY,
        title VARCHAR (255),
        writer VARCHAR (255),
        year INT(11)
        )
    '''
)

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS d4e12.actor(
            name VARCHAR (255)
        )
    '''
)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS d4e12.movie_actor(
        movie_id VARCHAR(255) REFERENCES d4e12.movie(_id),
        actor_name VARCHAR(255) REFERENCES d4e12.actor(name),
        PRIMARY KEY(movie_id, actor_name)
    )
    '''
)

# query = { #EXTRACT
#     'writer': {'$ne': None}, #khong duoc rong, co chua writer, ne = not equal
#     'year' : {'$ne': None},
#     'actors':{'$ne': None}
# }
# for movie in movie_collection.find(query): 
#     print(movie)
#    #TRANSFORM
#     movie_id = str(movie['_id'])
#     #LOAD
#     cursor.execute(
#         f'''
#         INSERT INTO d4e12.movie(_id, title, writer, year)
#         VALUES ('{movie_id}',
#         "{movie['title']}",
#         '{movie['writer']}',
#         {movie['year']}
#         )
#         '''
#     )
# mysql_client.commit()

#lenh aggregate cua mongodb
# query = [ #EXTRACT
#     {
#         '$unwind':'$actors'
#     },
#     {
#         '$group': {
#             '_id':'$actors'
#             # 'count':{$sum:1}
#         }
#     }
# ]

# for actor in movie_collection.aggregate(query):
#     cursor.execute(
#         f'''
#             INSERT INTO d4e12.actor(name)
#             VALUES ('{actor['_id']}')
#         '''
#     )

query = {
    'actors':{'$ne':None}
}
for movie in movie_collection.find(query):
    print(movie)
    for actor in movie['actors']:
        movie_id = str(movie['_id'])
        cursor.execute(
            f'''
            INSERT INTO d4e12.movie_actor(movie_id, actor_name)
            VALUES('{movie_id}','{actor}')
            '''
        )

mysql_client.commit()

# cursor.execute(
#     '''
#     SELECT * FROM d4e12.movie
#     '''
# )
# print(cursor.fetchall()) #fetchone 

# for i in movie_collection.find():
#     print(i)
