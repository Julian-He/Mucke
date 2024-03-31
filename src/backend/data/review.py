from dataclasses import dataclass
from typing import Dict, List
from discogs_client import Release

from user import User
from rating import Rating


@dataclass
class MusicSuggestion:
    user: User
    release: Release

@dataclass
class Review:
    host: User
    participants: List[User]
    music_suggestions: List[MusicSuggestion]
    ratings: List[Rating]