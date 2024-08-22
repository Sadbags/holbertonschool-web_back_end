#!/usr/bin/env python3
"""For reading CSV files
For mathematical operations (unused in this code)
For type hints
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get pages of popular baby names from dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        if (len(self.dataset()) < start_index) or (len(self.dataset()
                                                       ) < end_index):
            return []

        paginated_names = []
        for i in range(start_index, end_index):
            paginated_names.append(self.dataset()[i])

        return paginated_names

    @staticmethod
    def index_range(page, page_size) -> Tuple:
        """Calculate start and end indices for a given page and page size."""

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)
