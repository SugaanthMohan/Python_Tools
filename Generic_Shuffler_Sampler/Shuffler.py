# <<<<<<<<<<<<<<<<<< MODULES LIST >>>>>>>>>>>>>>>>>
# USED FOR SHUFFLING AROUND OBJECTS
import random
# IMPORT TIME LOGGER
from Utils.BenchMarker import seconds_benchmark


@seconds_benchmark
def basic_iterable_shuffler(iterables_):
    """
    Mutable Iterables shuffler
    :param iterables_: List of iterable container
    :return: shuffled iterables_
    """
    for index_1 in range(len(iterables_)-1, 0, -1):

        index_2 = random.randint(0, index_1 + 1)

        iterables_[index_1], iterables_[index_2] = iterables_[index_2], iterables_[index_1]

    return iterables_


@seconds_benchmark
def sampling_iterable_shuffler(iterables_):
    """
    Python Package based shuffler.
    :param iterables_: List of iterable container
    :return:
    """
    return random.sample(iterables_, len(iterables_))


@seconds_benchmark
def randomize_iterable_shuffler(iterables_):
    """
    Python Package based shuffler.
    :param iterables_: List of iterable container
    :return:
    """

    random.shuffle(iterables_, random=random.random)

    return iterables_

