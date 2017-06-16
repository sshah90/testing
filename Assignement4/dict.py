states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}


a=str(input("Give me any State name that you want to add :- "))
b=str(input("Give me Short form of state : "))



if a in states.keys():
    print("Name already in dict ")
else:
    states.update({a:b})

z=states.copy()
z.update(cities)


for i,j in z.items():
    print("after combine  ",i, "is",j)