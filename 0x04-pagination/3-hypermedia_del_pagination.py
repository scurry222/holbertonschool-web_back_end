#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) ->\
            Dict[str, Any]:
        """ If no data deletions, return a dictionary of information on data
            in index range. Else, skip through deleted indicies in index range.
        """
        assert type(index) is int and type(page_size) is int
        assert 0 <= index < len(self.indexed_dataset())
        page_end = min(index + page_size, len(self.indexed_dataset()))
        try:
            data = [self.indexed_dataset()[x] for x in range(index, page_end)]
        except Exception:
            data = self.get_hyper_index(index + 1, page_size)["data"]
            return {
                "index": index,
                "data": data,
                "page_size": page_size,
                "next_index": index + page_size + 1
            }
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": index + page_size
        }
