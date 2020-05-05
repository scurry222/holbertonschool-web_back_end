#!/usr/bin/env python3
'''
    Defines function wait_random
    Attributes:
        max_delay(int): default value of 10
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    ''' Async return random float from range 0 to max_delay '''
    rand = random.random() * max_delay
    await asyncio.sleep(rand)
    return rand
