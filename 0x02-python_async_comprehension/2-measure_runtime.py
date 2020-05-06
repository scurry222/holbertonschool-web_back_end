#!/usr/bin/env python3
'''
    Defines function measure_runtime
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''  '''
    total_time = time.time()
    await asyncio.gather(async_comprehension())
    return time.time() - total_time
