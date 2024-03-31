from dataclasses import dataclass
from typing import List

from review import Rating

@dataclass
class User:
    name: str
    ratings: List[Rating]