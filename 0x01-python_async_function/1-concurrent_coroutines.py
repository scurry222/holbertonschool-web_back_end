#!/usr/bin/env python3
'''
    Defines function wait_n
    Attributes:
        n(int): amount of times to call function wait_random
        max_delay(int): maximum value of delay
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    ''' Return array of delays from async function '''
    delays = []
    for i in range(n):
        delays += await asyncio.gather(wait_random(max_delay))
    return delays
