from dataclasses import dataclass
from typing import Dict, List
from discogs_client import Release

from user import User


@dataclass
class MusicSuggestion:
    user: User
    release: Release
    
@dataclass
class Rating:
    release: Release
    ratings: Dict[User, int]

class Review:
    def __init__(self, host: User, participants: List[User] = []) -> None:
        self.__host = host
        self.__participants = participants
        self.__music_suggestions: List[MusicSuggestion] = []
        self.__ratings: List[Rating] = []

        