from dataclasses import dataclass, field
from abc import ABC
from typing import Dict, List
from uuid import UUID, uuid1


def get_id() -> UUID:
    return uuid1()


@dataclass
class Album:
    title: str
    artist: str


@dataclass(kw_only=True)
class Review(ABC):
    id: UUID = field(default_factory=get_id)


@dataclass
class User:
    name: str
    reviews: List[Review]

    def __eq__(self, value: object) -> bool:
        if type(value) is User:
            return self.name is value.name
        else:
            return False

    def __hash__(self) -> int:
        return hash(str(self))


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
    id: UUID = field(default_factory=get_id)


@dataclass
class AppData:
    users: List[User]
    review_processes: List[ReviewProcess]
