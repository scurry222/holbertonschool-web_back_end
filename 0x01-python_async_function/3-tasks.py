#!/usr/bin/env python3
'''
    Defines function wait_random
    Attributes:
        max_delay(int): default value of 10
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' Async return random float from range 0 to max_delay '''
    return asyncio.create_task(wait_random())
