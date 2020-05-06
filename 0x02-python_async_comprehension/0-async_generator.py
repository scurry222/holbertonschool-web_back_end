#!/usr/bin/env python3
'''
    Defines function async_generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Create generator of random values '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
