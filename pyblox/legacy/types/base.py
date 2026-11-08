# Types that are shared across multiple APIs.

from enum import Enum


class Order(Enum):
    ASCENDING = "Asc"
    DESCENDING = "Desc"