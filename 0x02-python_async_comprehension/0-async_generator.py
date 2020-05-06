#!/usr/bin/env python3
'''
    Defines function async_generator
'''

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    ''' Create generator of random values '''
    for _i in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
