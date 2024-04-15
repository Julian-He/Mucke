from dataclasses import dataclass
from abc import ABC
from typing import Dict, List


@dataclass
class Album:
    title: str
    artist: str


@dataclass
class Review(ABC):
    pass


@dataclass
class User:
    name: str
    reviews: List[Review]


@dataclass
class Rating:
    score: int
    notes: str


@dataclass
class AlbumReview(Review):
    album: Album
    suggested_by: User
    scores: Dict[User, Rating]


@dataclass
class ReviewProcess:
    host: User
    participants: List[User]
    reviews: List[AlbumReview]


@dataclass
class AppData:
    users: List[User]
    review_processes: List[ReviewProcess]
