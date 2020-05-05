#!/usr/bin/env python3

'''
    Defines function sum_mixed_list
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Return sum of list containing ints OR floats '''
    return sum(mxd_lst)
