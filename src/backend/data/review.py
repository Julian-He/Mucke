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

@dataclass
class Review:
    host: User
    participants: List[User]
    music_suggestions: List[MusicSuggestion]
    ratings: List[Rating]