from dataclasses import dataclass
from typing import List

from review import Review
from user import User

@dataclass
class AppData:
    users: List[User]
    reviews: List[Review]