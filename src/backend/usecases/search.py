from typing import List
from uuid import UUID

from ..data import AlbumReview, AppData, ReviewProcess, User


def search_users(appdata: AppData, search: str) -> List[User]:
    result: List[User] = []

    for user in appdata.users:
        if user.name.upper() == search.upper():
            result.append(user)

    return result


def search_review_processes(appdata: AppData, id: UUID) -> ReviewProcess | None:
    for review_proc in appdata.review_processes:
        if review_proc.id == id:
            return review_proc


def search_album_review(process: ReviewProcess, id: UUID) -> AlbumReview | None:
    for review in process.reviews:
        if review.id == id:
            return review
