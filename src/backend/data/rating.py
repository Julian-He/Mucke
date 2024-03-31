from dataclasses import dataclass
from discogs_client import Release
from typing import Dict

from user import User

@dataclass
class Rating:
    release: Release
    ratings: Dict[User, int]