import random,json


def random_data(tuple_size = 2):
    return tuple(random.randint(1, 100)/random.randint(1, 100) for _ in range(tuple_size))

def random_data_list(list_size = 10):
    data_set = set()
    while len(data_set) < list_size:
        data_set.add(random_data())
    return list(data_set)
    
def generate_C0(data_list):
    mapped_dict = {index: value for index, value in enumerate(data_list)}
    print(mapped_dict)

    json_output = json.dumps(mapped_dict, indent=4)
    print(json_output)

    # Save to a file (optional)
    with open("./C0.json", "w") as json_file:
        print("Hit!")
        json_file.write(json_output)

generate_C0(random_data_list())