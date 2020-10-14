import itertools


def test_product_combinator(container_, repeat_times):
    """
    cartesian product, equivalent to a nested for-loop

    product('ABCD', repeat=2)
    AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
    """

    return list(itertools.product(container_, repeat=repeat_times))


def test_permutation_combinator(container_, pairs_):
    """
    r-length tuples, all possible orderings, no repeated elements

    permutations('ABCD', 2)
    AB AC AD BA BC BD CA CB CD DA DB DC
    """

    return list(
        itertools.permutations(
            container_,
            pairs_
        )
    )


def test_combination_combinator(container, pairs_):
    """
    r-length tuples, in sorted order, no repeated elements

    combinations('ABCD', 2)
    AB AC AD BC BD CD
    """
    return list(
        itertools.combinations(container, pairs_)
    )


def test_combinations_with_replacement_combinator(container, pairs_):
    """
    r-length tuples, in sorted order, no repeated elements

    combinations('ABCD', 2)
    AB AC AD BC BD CD
    """
    return list(
        itertools.combinations_with_replacement(container, pairs_)
    )


if __name__ == '__main__':

    count = 10

    items_list = list(
        map(
            lambda x: str(x[0]) + "_" + str(x[1]),
            list(
                zip(
                    ['TYPE'] * count,
                    list(range(1, count+1))
                )
            )
        )
    )

    print(items_list)
    print("PRODUCT :=>", test_product_combinator(container_=items_list, repeat_times=2))
    print("PERMUTATIONS :=>", test_permutation_combinator(container_=items_list, pairs_=2))
    print("COMBINATIONS :=>", test_combination_combinator(container=items_list, pairs_=2))
    print("COMBINATIONS WITH REPLACEMENT :=>", test_combinations_with_replacement_combinator(container=items_list, pairs_=2))

