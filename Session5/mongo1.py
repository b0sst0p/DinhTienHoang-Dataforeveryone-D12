from pymongo import MongoClient 
client = MongoClient() #connect to mongodb server
db = client.get_database('allcake') #get db name
allcake_collection = db.get_collection('cake') #get collection name
cakelist = {
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
allcake_collection.insert_one(cakelist) #insert a record to collection
cake = allcake_collection.find() #GET all records
for allcake in cake:
    pass
print(allcake['items']['item'][0])