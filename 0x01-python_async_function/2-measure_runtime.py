#!/usr/bin/env python3
'''
    Defines function measure_time
    Attributes:
        n(int): amount of times to call function wait_random
        max_delay(int): maximum value of delay
'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Measures total execution time for wait_n '''
    total_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - total_time
    return total_time / n
