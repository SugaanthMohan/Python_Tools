import itertools
import io


def validate_accumulate(container_):
    """
    accumulate([1,2,3,4,5]) --> 1 3 6 10 15

    """
    return list(
        itertools.accumulate(
            container_
        )
    )


def validate_chain(container_list_):
    """
    NAME : chain()
    Arguments : p, q, …
    Results : p0, p1, … plast, q0, q1, …
    Example : chain('ABC', 'DEF') --> A B C D E F
    """

    return list(itertools.chain(*container_list_))


def validate_chain_from_iterable(container_list_):
    """
    NAME : chain.from_iterable()
    Arguments : iterable
    Results : p0, p1, … plast, q0, q1, …
    Example : chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    """

    return list(itertools.chain.from_iterable(container_list_))


def validate_compress(container_, sequence_):
    """
    NAME : compress()
    Arguments : data, selectors
    Results : (d[0] if s[0]), (d[1] if s[1]), …
    Example : compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    """

    return list(
        itertools.compress(container_, sequence_)
    )


def validate_dropwhile(condition_, container_):
    """
    NAME : dropwhile()
    Arguments : pred, seq
    Results : seq[n], seq[n+1], starting when pred fails
    Example : dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    """

    return list(
        itertools.dropwhile(
            condition_,
            container_
        )
    )


def validate_filterfalse(condition_, container_):
    """
    NAME : filterfalse()
    Arguments : pred, seq
    Results : elements of seq where pred(elem) is false
    Example : filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    """

    return list(
        itertools.filterfalse(
            condition_,
            container_
        )
    )


def validate_groupby(container_, key_function_):
    """
    NAME : groupby()
    Arguments : iterable[, key]
    Results : sub-iterators grouped by value of key(v)
    Example : nan
    """

    return [
        [key] + list(item) for key, item in itertools.groupby(container_, key_function_)
    ]


def validate_islice(container_, start_=None, stop=None, step=None):
    """
    NAME : islice()
    Arguments : seq, [start,] stop [, step]
    Results : elements from seq[start:stop:step]
    Example : islice('ABCDEFG', 2, None) --> C D E F G
    """

    return list(
        itertools.islice(container_, start_, stop, step)
    )


def validate_starmap(operation_, conatiner_):
    """
    NAME : starmap()
    Arguments : func, seq
    Results : func(*seq[0]), func(*seq[1]), …
    Example : starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    """

    return itertools.starmap(operation_, conatiner_)


def validate_takewhile(operation_, container_):
    """
    NAME : takewhile()
    Arguments : pred, seq
    Results : seq[0], seq[1], until pred fails
    Example : takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    """
    return list(
        itertools.takewhile(operation_, container_)
    )


def validate_tee(iterator_, split_count_):
    """
    NAME : tee()
    Arguments : it, n
    Results : it1, it2, … itn splits one iterator into n
    Example : nan
    """

    return [
        itertools.tee(iterator_, split_count_)
    ]


def validate_zip_longest(container_, fill_val='-'):
    """
    NAME : zip_longest()
    Arguments : p, q, …
    Results : (p[0], q[0]), (p[1], q[1]), …
    Example : zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    """

    return list(
        itertools.zip_longest(*container_, fillvalue=fill_val)
    )


if __name__ == '__main__':
    # List = list(range(18))
    # print(List)
    # print(validate_accumulate(List))
    # chainer_test_input = list(zip(*(iter(range(100)), ) * 10))
    # print(chainer_test_input)
    # print(validate_chain(container_list_=chainer_test_input))
    # print(validate_chain_from_iterable(container_list_=chainer_test_input))
    # compress_elements_count = 50
    # compress_elements_list = list(
    #     map(
    #         lambda x: str(x[1]) + "_" + str(x[0]),
    #         enumerate(
    #             list(
    #                 itertools.repeat('ELEMENT', compress_elements_count)
    #             ),
    #             start=1
    #         )
    #     )
    # )
    #
    # compress_filter = [
    #     random.choice([0, 1]) for _ in range(compress_elements_count)
    # ]
    #
    # print("COUNT OF ELEMENTS :", compress_elements_count)
    # print("ELEMENTS :", compress_elements_list)
    # print("FILTER :", compress_filter)
    # print("OUTPUT :", validate_compress(container_=compress_elements_list, sequence_=compress_filter))

    # drop_while_condition = lambda val: val < 50
    # sequence = list(range(1, 101))
    #
    # print("ELEMENTS :", sequence)
    # print("OUTPUT :", validate_dropwhile(condition_=drop_while_condition, container_=sequence))

    # HPI INPUT SAMPLES
    #     data = """hpi_type,hpi_flavor,frequency,level,place_name,place_id,yr,period,index_nsa,index_sa
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,1,100.00,100.00
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1992,1,103.94,103.96
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1992,2,104.40,104.46
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,2,101.00,101.08
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,3,101.36,100.98
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,4,101.75,101.04
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,5,102.39,101.44
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,6,102.82,101.56
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,7,103.01,101.90
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,8,103.17,102.09
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,9,102.88,102.06
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,10,103.10,102.41
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,11,104.01,103.36
    # "traditional","purchase-only","monthly","USA or Census Division","East North Central Division","DV_ENC",1991,12,103.78,103.47"""
    #
    #     columns = data.split('\n')[0]
    #
    #     hpi_ds = [
    #         row.split(',')
    #         for row in data.split('\n')[1:]
    #     ]
    #
    #     sorting_group = lambda x: x[-3]
    #
    #     print(validate_groupby(hpi_ds, sorting_group))
    #
    #

    # CUSTOM FUNCTION FOR STAR MAP

    # sequence = list(range(1, 5, 1))
    # count = 2
    # inp = list(itertools.combinations_with_replacement(sequence, 2))
    # print(sequence)
    # print(inp)
    # operation = pow
    # print(str(validate_starmap(operation, sequence)))

    # sequence = range(1, 10, 2)
    # condition = lambda x: x < 7
    #
    # print(validate_takewhile(condition, sequence))

    # tee_sequence = list(range(10))
    # print(tee_sequence)
    # splits = 2
    #
    # for idx, iter_obj in enumerate(validate_tee(tee_sequence, splits)):
    #     for val in iter_obj:
    #         print(idx, " : ", *val)

    splits = 10
    val_size = 30
    inps = list(zip(*(iter(range(val_size)), ) * splits))

    print(validate_zip_longest(container_=inps, fill_val=999))




