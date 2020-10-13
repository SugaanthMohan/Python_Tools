# <<<<<<<<<<<<<<<<<< MODULES LIST >>>>>>>>>>>>>>>>>
# USED FOR DECORATOR CREATION
from functools import wraps
# TIME MODULE FOR TIME CALCULATION
import time


def seconds_benchmark(function_wrapper):
    """
    outer wrapper function to perform inner wrap for seconds benchmark.
    :param function_wrapper: The entire function object.
    :return:
    """

    @wraps(function_wrapper)
    def wrap(*args, **kwargs):
        """

        :param args: positional args
        :param kwargs: keyword args
        :return:
        """
        start_time = time.time()
        result = function_wrapper(*args, **kwargs)
        print("========================== DEBUGGER START =====================")
        print("Function : %r" % function_wrapper.__name__)
        print("Args : %r" % str(args)[:50])
        print("P-Args : %r" % str(kwargs)[:50])
        print("Elapsed Time : %.3f Sec(s)" % (time.time() - start_time))
        print("========================== DEBUGGER END =======================\n\n\n")
        return result

    return wrap
