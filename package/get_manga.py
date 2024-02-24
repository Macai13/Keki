from collections.abc import Mapping
import requests
import mangadex

def get_manga(manga_title: str):
    api = mangadex.Api()

    return api.get_manga_list(title=manga_title)