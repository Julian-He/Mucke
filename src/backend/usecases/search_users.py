from typing import List

from data import AppData, User

def searchUsers(appdata: AppData, search: str) -> List[User]:
    result: List[User] = []

    for user in appdata.users:
        if user.name.capitalize == search.capitalize:
            result.append(user)

    return result
