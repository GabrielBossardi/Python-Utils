import time
from typing import List, Dict, Set

def _squared_num(num: int) -> int:
    time.sleep(.5)
    return num**2

def list_comprehension() -> None:
    squared_list = [_squared_num(i) for i in range(10)]
    print(squared_list)

def dict_comprehension() -> None:
    car_list: List[str] = ['Ferrari', 'Lamborghini', 'Porsche']
    car_dict: Dict[str, str] = {f'{element.lower()}': f'Assembler: {element.upper()}' for element in car_list}
    print(car_dict)

    car_dict = {
        f'{element.lower()}' if element != 'Porsche' else 'Other':
        f'Assembler: {element.upper()}' for element in car_list}
    print(car_dict)

def set_comprehension() -> None:
    squared_set: Set[int] = {_squared_num(i) for i in range(10)}
    [print(i) for i in squared_set]

if __name__ == '__main__':
    list_comprehension()
    dict_comprehension()
    set_comprehension()
