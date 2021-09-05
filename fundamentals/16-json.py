import json

data = {
    "name": "Kevin",
    "age": 23,
    "favourite_foods": [
        "pizza",
        "bagels",
        "watermelon"
    ]
}


def print_as_json(data):
    as_basic_json = json.dumps(data)
    print(as_basic_json)
    as_fancy_json = json.dumps(data, indent=4)
    print(as_fancy_json)


print_as_json(data)

json_data = '{ "name":"John", "age":30, "city":"New York"}'
data = json.loads(json_data)
print()
print(f"Name is: {data['name']}")
print(f"City is: {data['city']}")
