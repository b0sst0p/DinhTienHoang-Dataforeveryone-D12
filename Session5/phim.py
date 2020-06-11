from pymongo import MongoClient

client = MongoClient()

db = client.get_database('d4e12')

movie_collection = db.get_collection('movie') # tao record. 
data = [
{
  'title' : 'Fight Club',
  'writer' : 'Chuck Palahniuk',
  'year' : 1999,
  'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
},
{
  'title' : 'Pulp Fiction',
  'writer' : 'Quentin Tarantino',
  'year' : 1994,
  'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
},
{
  'title' : 'Inglorious Basterds',
  'writer' : 'Chuck Palahniuk',
  'year' : 2009,
  'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
},
{
  'title' : 'The Hobbit: An Unexpected Journey',
  'writer' : 'Chuck Palahniuk',
  'year' : 2012,
  'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ],
  'franchise' : 'The Hobbit'  ,
},
{
  'title' : 'The Hobbit: The Desolation of Smaug',
  'writer' : 'Chuck Palahniuk',
  'year' : 2013,
  'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ],
  'franchise' : 'The Hobbit'
},
{
  'title' : 'The Hobbit: The Battle of the Five Armies',
  'writer' : 'Chuck Palahniuk',
  'year' : 2012,
  'actors' : [
    'Brad Pitt', 
    'Edward Norton',
  ],
  'franchise' : 'The Hobbit',
  'synopsis' : 'Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness.'
},
{
'title' : "Pee Wee Herman's Big Adventure",
},
{
'title' : 'Avatar',
},
]

movie_collection.insert_many(data)
# movie = movie_collection.find() #get all record
# # # for i in movie: #print lan luot tung dong record
# #   print(i)

# # for i in movie_collection.find({'writer': 'Quentin Tarantino'}) : #print movie title has name Quentin Tarantino
# #   print(i)

# # # for i in movie_collection.find({'actors': 'Brad Pitt'}) : #print movie title has actors: Brad Pitt
# # #   print(i)

# # # for i in movie_collection.find({'franchise': 'The Hobbit'}) : #print movie title has franchise: The Hobbit
# # #   print(i)

# # for movie_90 in movie_collection.find({ 'year': { '$lt': 2000 } } ) : #print movie title has release year in 90s, lt: less than. 
# #   print(movie_90)
 
# for movie_90 in movie_collection.find( { $or: [ { year: { $lt: 2000 } }],[{ year: { $gt: 2010 } }] ): 
#   #print movie title has release year before 2000 or after 2010, $or: for requirement between 2 ranges. 
#   print(movie_90)





