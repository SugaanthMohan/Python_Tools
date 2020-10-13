import itertools


def infinite_cycle_int(start_: int = 0, step_: int = 1, max_: int = 10) -> int:
    """
    :param start_:
    :param step_:
    :param max_:
    :yield integer number
    """

    for integer in itertools.count(start_, step_):
        if max_ == 0:
            break
        max_ -= 1
        yield integer


def cycle_through_elements(elements_, max_: int = 10):
    """
    :param elements_:
    :param max_:
    :return None
    """

    for element in itertools.cycle(elements_):
        if max_ == 0:
            break
        else:
            yield element
        max_ -= 1


def repeater(item_, counter_):
    """
    :param item_: the item to repeat
    :param counter_: the total number of items to be repeated
    :return list
    """

    return [
        *(
            itertools.repeat(item_, counter_)
        )
    ]


if __name__ == '__main__':
    # for item in infinite_cycle_int(10, 5, 30):
    #     print(item)
    # for item in cycle_through_elements("ABCDEFGHIJKL", max_=20):
    #     print(item)
    print(repeater(20, 20))
