class MyFirstClass(object):
    MAX_WORDS = 10

    @classmethod
    def what_is_class(cls):
        print(cls)

    def what_is_instance(self):
        print(self)

    def __init__(self):
        self._my_words = list()

    def store_a_word(self, word: str):
        self._my_words.append(word)

    def print(self):
        for _word in self._my_words:
            print(_word)


if __name__ == "__main__":
    my_class = MyFirstClass()
    my_other_class = MyFirstClass()

    my_class.store_a_word("first")
    my_class.store_a_word("second")

    my_other_class.store_a_word("I am getting lazy")
    my_other_class.store_a_word("Really really lazy")

    print("First class:")
    my_class.print()
    print()
    print("Second class:")
    my_other_class.print()

    print("Existential crisis:")
    my_class.what_is_class()
    my_class.what_is_instance()
    my_other_class.what_is_instance()
