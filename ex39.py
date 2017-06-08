
state = {
'Oregon': 'OR',
'Florida':'FL',
'California': 'CA',
'New York' : 'NY',
'Michigan' : 'MI'
}

cities={
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}

cities['NY']='New York'
cities['OR'] = 'Portland'


print '--'*10
print "NY State has:",cities['NY']
print "OR State has:",cities['OR']

print '--'*10
print "Michigan's abbreviation is :",state['Michigan']
print "Florida's abbreviation is :",state['Florida']

print '--'*10
print "Michigan has:",cities[state['Michigan']]
print "Florida has:",cities[state['Florida']]

print '--'*10
for state,abbrev in state.items():
	print "%s is abbreviated %s" %(state,abbrev)

print '--'*10
for abbrev,city in cities.items():
	print "%s has the city %s" %(abbrev,city)

print '--'*10
for states,abbrev in state .items():
	print "%s state  is abbreviated %s and has city %s" % (
		states,abbrev,cities[abbrev])

print '--'*10
states = state.get('Texas',none)

if not states:
	print "Sorry,no Texas"

city = cities.get('TX','Does not Exist')
print "The city for the state 'TX' is :%s" %city
