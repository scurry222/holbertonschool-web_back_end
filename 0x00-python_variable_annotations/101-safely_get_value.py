#!/usr/bin/env python3
'''
    Defines function safely_get_value
'''

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]=None) -> Union[Any, T]:
    ''' Return dct[key] if it exists, otherwise return the default '''
    if key in dct:
        return dct[key]
    else:
        return default
