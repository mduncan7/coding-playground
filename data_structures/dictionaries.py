my_dict = {
    "top_level_key_one": "val_one",
    "top_level_key_two": "val_two",
    "top_level_key_three": "val_three"
}


class Animal(object):
    def __init__(self, animal_type: str, ave_weight: float):
        self.type = animal_type
        self.ave_weight = ave_weight


nested_one = {
    "mammals": ["dog", "cat", "rabbit"],
    "reptiles": ["lizard", "alligator", "tortoise"],
    "insects": ["fucking-gross-bug", "other-fucking-gross-bug"]
}
nested_two = {
    "mammals": [
        {"type": "dog", "ave_weight": 2.0},
        {"type": "cat", "ave_weight": 1.0},
        {"type": "rabbit", "ave_weight": 0.6}
    ],
    "reptiles": [
        {"type": "lizard", "ave_weight": 0.5},
        {"type": "alligator", "ave_weight": 3.5},
        {"type": "tortoise", "ave_weight": 2.0}
    ],
    "insects": [
        {"type": "fucking-gross-bug", "ave_weight": 0.002},
        {"type": "other-fucking-gross-bug", "ave_weight": 0.001}
    ]
}
nested_three = {
    "mammals": [
        Animal("dog", 2.0),
        Animal("cat", 1.0),
        Animal("rabbit", 0.6)
    ]
}


def basics():
    for k, v in my_dict.items():
        print(f"{k} = {v}")

    reversed_dict = {}
    for k, v in my_dict.items():
        reversed_dict[v] = k

    reversed_dict = {my_val: my_key for my_key, my_val in my_dict.items()}


def a_little_complex():
    for animal_class, list_of_animals in nested_one.items():
        print(f'Here are some {animal_class}:')
        for animal in list_of_animals:
            print(f'\t{animal}')


# Here are some mammals:
#    dog
#    cat
#    rabbit

if __name__ == "__main__":
    a_little_complex()
