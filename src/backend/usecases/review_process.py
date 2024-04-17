from uuid import UUID
from backend.data import Album, AlbumReview, AppData, ReviewProcess, User


def start_review_process(appdata: AppData, host: User, hosts_pick: Album) -> UUID:
    review = ReviewProcess(host, [], [AlbumReview(hosts_pick, host, {})])
    appdata.review_processes.append(review)

    return review.id