from uuid import UUID
from ..data import AppData, Rating, User


def submit(
    appdata: AppData,
    processID: UUID,
    reviewID: UUID,
    user: User,
    rating: int,
    notes: str,
):
    for process in appdata.review_processes:
        if process.id == processID:
            for review in process.reviews:
                if review.id == reviewID:
                    review.scores[user] = Rating(rating, notes)
