#!/usr/bin/env python3

'''
    Defines function make_multiplier
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Return function that multiplies float by multiplier '''
    return lambda x: x * multiplier
