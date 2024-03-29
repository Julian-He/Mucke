from dataclasses import dataclass
from typing import List

from review import Review

@dataclass
class User:
    name: str
    reviews: List[Review]