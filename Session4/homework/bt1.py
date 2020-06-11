inventory = {
'gold' : [500],
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ["​sashell", "strangeberry" , "lint"]
print(inventory)

removed_inventory = inventory['backpack']
del removed_inventory['dagger']
print(inventory)


