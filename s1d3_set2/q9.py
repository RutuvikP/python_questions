sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
output={}

for key in keys:
    if sample_dict[key]:
        output[key]=sample_dict[key]

print(output)