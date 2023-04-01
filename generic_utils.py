import math
from typing import List


def slicing_list(lst: List, chunksize: int) -> List[List]:
    sliced_list = []

    for i in range(math.ceil(len(lst) / chunksize)):
        sliced_list.append(lst[i * chunksize:i * chunksize + chunksize])

    return sliced_list
