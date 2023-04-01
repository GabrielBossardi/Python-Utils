class IteratorTest:

    def __init__(self, maximum: int = 1000000) -> None:
        self.current_element: int = 0
        self.next_element: int = 1
        self.maximum: int = maximum

    def __iter__(self) -> 'IteratorTest':
        # Return itself
        return self

    def __next__(self) -> int:
        # End of iteration, raise StopIteration
        if self.current_element > self.maximum:
            raise StopIteration
        # It saves the value to be returned
        returned_value: int = self.current_element
        # It updates the next sequence element
        self.current_element, self.next_element = self.next_element, self.current_element + self.next_element
        return returned_value


if __name__ == '__main__':
    fibonacci_object: IteratorTest = IteratorTest(maximum=100)

    for fibonacci in fibonacci_object:
        print("Sequencia: {}".format(fibonacci))
