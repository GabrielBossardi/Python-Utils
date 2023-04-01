import time
from typing import Generator


def genenerator_test(maximum: int = 1000) -> Generator[int, None, None]:
    current_element, next_element = 0, 1

    while current_element < maximum:
        time.sleep(.5)
        yield current_element

        current_element, next_element = next_element, current_element + next_element


if __name__ == '__main__':
    fibonacci_object = genenerator_test(maximum=100)

    for fibonacci in fibonacci_object:
        print("Sequencia: {}".format(fibonacci))
