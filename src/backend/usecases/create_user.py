from backend.data.appdata import AppData
from backend.data.user import User


def create_user(appdata: AppData, name: str) -> AppData:
    user: User = User(name, [])
    appdata.users.append(user)
    return appdata