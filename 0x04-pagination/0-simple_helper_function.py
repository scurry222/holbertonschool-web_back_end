#!/usr/bin/env python3
""" Defines function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return range of items within current page(1 indexed) """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
