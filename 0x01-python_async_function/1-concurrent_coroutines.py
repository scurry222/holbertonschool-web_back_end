#!/usr/bin/env python3
'''
    Defines function wait_n
    Attributes:
        n(int): amount of times to call function wait_random
        max_delay(int): maximum value of delay
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' Return array of delays from async function '''
    delays: List[float] = []
    for i in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return [await delay for delay in asyncio.as_completed(delays)]
