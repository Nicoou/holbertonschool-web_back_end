#!/usr/bin/env python3
""" task 2 """

import csv
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
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
                split[len(split) - 1] = split[len(split) - 1].strip("\n")
                content.append(split)
        return content

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """def hyper"""
        hyper = {}
        with open("Popular_Baby_Names.csv", "r") as file:
            read = file.readlines()
            hyper["page_size"] = page_size
            hyper["page"] = page
            hyper["data"] = self.get_page(page, page_size)
            if not hyper["data"]:
                hyper["page_size"] = 0
            hyper["total_pages"] = int(len(read) / page_size)
            if page == hyper["total_pages"]:
                hyper["next_page"] = None
            else:
                hyper["next_page"] = page + 1
            hyper["prev_page"] = None if page < 2 else page - 1
        return hyper
