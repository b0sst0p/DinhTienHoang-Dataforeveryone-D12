from pymongo import MongoClient
from bson import ObjectId
client = MongoClient()

db = client.get_database('d4e12')

cake_collection = db.get_collection('cake')

data = {
	"items":
		{
			"item":
				[
					{
						"id": "0001",
						"type": "donut",
						"name": "Cake",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
										{ "id": "1002", "type": "Chocolate" },
										{ "id": "1003", "type": "Blueberry" },
										{ "id": "1004", "type": "Devil's Food" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
								{ "id": "5007", "type": "Powdered Sugar" },
								{ "id": "5006", "type": "Chocolate with Sprinkles" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					},
					{
						"id": "0002",
						"type": "donut",
						"name": "Raised",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					},
		
					{
						"id": "0003",
						"type": "donut",
						"name": "Old Fashioned",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
										{ "id": "1002", "type": "Chocolate" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					},
					{
						"id": "0004",
						"type": "bar",
						"name": "Bar",
						"ppu": 0.75,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
									]
							},
						"topping":
							[
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							],
						"fillings":
							{
								"filling":
									[
										{ "id": "7001", "name": "None", "addcost": 0 },
										{ "id": "7002", "name": "Custard", "addcost": 0.25 },
										{ "id": "7003", "name": "Whipped Cream", "addcost": 0.25 }
									]
							}
					},

					{
						"id": "0005",
						"type": "twist",
						"name": "Twist",
						"ppu": 0.65,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
									]
							},
						"topping":
							[
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
							]
					},

					{
						"id": "0006",
						"type": "filled",
						"name": "Filled",
						"ppu": 0.75,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
									]
							},
						"topping":
							[
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5007", "type": "Powdered Sugar" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							],
						"fillings":
							{
								"filling":
									[
										{ "id": "7002", "name": "Custard", "addcost": 0 },
										{ "id": "7003", "name": "Whipped Cream", "addcost": 0 },
										{ "id": "7004", "name": "Strawberry Jelly", "addcost": 0 },
										{ "id": "7005", "name": "Rasberry Jelly", "addcost": 0 }
									]
							}
					}
				]
		}
}

cakes_list = data['items']['item']

# for cake in cakes_list:
#     cake_collection.insert_one(cake)

#sua cake thanh banh
#can biet thong tin no sua bang ghi nao, sua thong tin nao trong bang ghi day
#dien 2 thogn tin, trong () 2 cuc dictionary
# query = {                                                 # neu query ko ghi gi thi la sua tat ca
#     '_id': ObjectId('5ecbcea0bd6751099b024fff')
# }
# update = {
#     '$set': { #cau lenh cua mongo db co dau $: mo ta hanh dong
#         'name': 'banh'
#     }
# }
# cake_collection.update_one(query, update)
# # cake_collection.update_one() co the thay the one thanh many ben trong la 1 list

# # lay objectID
# # cakes = cake_collection.find()
# # for cake in cakes:
# #     print(cake)

# # for cake in cakes_list:
# #     cake_collection.insert_one(cake)

# # cake_collection.insert_many(cakes_list)

# cake_collection.delete_one(query) #delete ban ghi minh can xoa

