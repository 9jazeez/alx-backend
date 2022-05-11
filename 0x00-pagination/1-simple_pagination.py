#!/usr/bin/env python3
""" A module for example pagination """

import csv
import math
from typing import List


def index_range(page, page_size):
    """A function that takes in a page 
     -page no
     -page size
     returns a tuple.
    """
    if page and page_size:
        st_index = (page - 1) * page_size
        end = st_index + page_size
    tup = (st_index, end)
    return tup


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
		""" Obtain index and return Page from REST API """
		assert type(page) == int and page > 0
		assert type(page_size) == int and page_size > 0
		st_page, end_page = index_range(page, page_size)
		page_result = []

		if st_page >= len(self.dataset()):
			return page_result
		page_result = self.dataset()

		return page_result[st_page:end_page]
		
