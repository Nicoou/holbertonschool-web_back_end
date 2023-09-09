#!/usr/bin/env python3
""" task 3 """

import csv
from typing import List, Dict


def index_range(page, page_size):
    """def index"""
    return ((page - 1) * page_size, page_size * page)


class Server:
    """server class"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """def dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                dataset = [row for row in read]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """def index"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {n: dataset[n] for n in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """def hyper"""
        index_data = self.indexed_dataset()

        assert 0 <= index < len(index_data)

        coll = {}
        coll["index"] = index

        data = []
        next_index = index

        while len(data) < page_size and next_index in index_data:
            if next_index in index_data:
                data.append(index_data[next_index])
            next_index += 1
        coll["data"] = data
        coll["page_size"] = page_size
        coll["next_index"] = next_index

        return coll
