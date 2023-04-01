import time


def squared_num(num):
    time.sleep(.5)
    return num**2

if __name__ == '__main__':
    squared_list = (squared_num(i) for i in range(10))
    [print(i) for i in squared_list]
