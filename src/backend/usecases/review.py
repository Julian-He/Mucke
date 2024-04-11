from typing import List
from discogs_client import Release

from data import User, ReleaseReview, ReviewProcess, AppData

def start_review(all_users: List[User], host: User, hosts_pick: Release) -> AppData:
    AppData.review_processes.append(
        ReviewProcess(host, [], ReleaseReview(
            hosts_pick, host, [,])
        ))
        )    
