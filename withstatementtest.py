
class TestWith:
    def __init__(self):
        self.coucou = "coucou"

    def display_coucou(self):
        print(self.coucou)

    def __enter__(self):
        print("Enter method called")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit method called")


class Saved:
    def __init__(self, word):
        self.word = word

    def __enter__(self):
        print("".join(["In enter method", self.word]))
        return self.word

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("In exit method")


def test_with_statement():
    print("First test")
    print("----------------")
    with TestWith() as test:
        test.display_coucou()

    print()
    print("Second test")
    print("----------------")
    with Saved("Word") as word:
        print("".join(["In the block", word]))
