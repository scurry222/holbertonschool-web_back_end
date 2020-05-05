#!/usr/bin/env python3
'''
    Defines function wait_n
    Attributes:
        n(int): amount of times to call function wait_random
        max_delay(int): maximum value of delay
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' Return array of delays from async function '''
    delays: List[float] = []
    for i in range(n):
        delays += await asyncio.gather(task_wait_random(max_delay))
    return delays
