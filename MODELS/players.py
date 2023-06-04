with open('../Data/new-tournament/currentDate') as user_file:
  file_contents = user_file.read()
  
print(file_contents)
# {
#   "name": "John",
#   "age": 50,
#   "is_married": false,
#   "profession": null,
#   "hobbies": ["travelling", "photography"]
# }