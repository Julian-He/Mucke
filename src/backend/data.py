from dataclasses import dataclass
from abc import ABC
from typing import Dict, List
from uuid import UUID, uuid4


@dataclass
class Album:
    title: str
    artist: str


@dataclass(kw_only=True)
class Review(ABC):
    id: UUID = uuid4()


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
    id: UUID = uuid4()


@dataclass
class AppData:
    users: List[User]
    review_processes: List[ReviewProcess]
