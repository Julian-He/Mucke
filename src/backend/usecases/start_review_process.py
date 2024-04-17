from backend.data import Album, AlbumReview, AppData, ReviewProcess, User


def start_review_process(appdata: AppData, host: User, hosts_pick: Album):
    appdata.review_processes.append(
        ReviewProcess(host, [], [AlbumReview(hosts_pick, host, {})])
    )
