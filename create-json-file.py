import json

# Data to be written
dictionary = '{ "name": "sathiyajith", "rollno": 56, "cgpa": 8.6, "phonenumber": "9976770500"}'

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)




# # JSON data:
# x =  '{ "organization":"GeeksForGeeks", "city":"Noida", "country":"India"}'

# python object to be appended
y = {"pin":110096}

# parsing JSON string:
z = json.loads(dictionary)

# appending the data
z.update(y)

# the result is a JSON string:
print(json.dumps(z))













