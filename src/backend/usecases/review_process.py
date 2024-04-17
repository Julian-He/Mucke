from uuid import UUID
from ..data import Album, AlbumReview, AppData, ReviewProcess, User


def start_review_process(appdata: AppData, host: User, hosts_pick: Album) -> UUID:
    review = ReviewProcess(host, [host], [AlbumReview(hosts_pick, host, {})])
    appdata.review_processes.append(review)

    return review.id


def add_user(appdata: AppData, process_id: UUID, user: User) -> None:
    for process in appdata.review_processes:
        if process.id == process_id:
            process.participants.append(user)
