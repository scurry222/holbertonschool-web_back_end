#!/usr/bin/env python3

'''
    Defines function element_length
'''

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Return list of tuples containing element and index '''
    return [(i, len(i)) for i in lst]
