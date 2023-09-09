#!/usr/bin/env python3
""" task 1 """

import csv
import math
from typing import List


def index_range(page, page_size):
    """def index"""
    return ((page - 1) * page_size, page_size * page)


class Server:
    """server class"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """def dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                read = csv.reader(f)
                dataset = [row for row in read]
            self.__dataset = dataset[1:]
        
        return self.__dataset
    
    def get_page(self, page: int = 1, page_size: int = 10) -> list[list]:
        """def get"""
        assert isinstance(page_size, int)
        assert isinstance(page, int)
        assert page_size > 0
        assert page_size > 0
        content = []
        index = index_range(page, page_size)
        with open("Popular_Baby_Names.csv", "r") as file:
            read = file.readlines()
            if len(read) < page * page_size:
                return []
            for n in range(index[0] + 1, index[1] + 1):
                split = read[n].split(",")
                split[len(read) - 1] = split[len(read) - 1].strip(
                    "\n"
                )
                content.append(split)
        return content
