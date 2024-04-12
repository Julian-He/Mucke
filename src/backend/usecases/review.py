from typing import List
from discogs_client import Release

from data import User, ReleaseReview, ReviewProcess, AppData


def start_review(appdata: AppData, host: User, hosts_pick: Release) -> AppData:
    appdata.review_processes.append(
        ReviewProcess(host, [], [ReleaseReview(hosts_pick, host, {})])
    )

    return appdata
