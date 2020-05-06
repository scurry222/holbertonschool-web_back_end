#!/usr/bin/env python3
'''
    Defines function async_generator
'''
import asyncio
import random
from typing import Generator


async def async_generator():
    ''' Create generator of random values '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
