import json

# dictionary => key -value


#person = {"name":"Rahmetullah","languages":["python","C"]}

# print(person["name"])
# print(person["languages"][1])

person_stirng = '{"name":"Rahmetullah","languages":["python","C"]}'

#json string to dict

result=json.loads(person_stirng)
print(result)
print(type(result))