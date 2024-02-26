import mangadex
import requests

def get_manga(manga_title: str):
    api = mangadex.Api()

    manga_list = api.get_manga_list(title=manga_title)
    manga_id = manga_list[0].manga_id

    return manga_id


def get_chapter_id(chapter_index: str, manga_id: str):
    base_url = "https://api.mangadex.org"

    r = requests.get(
        f"{base_url}/manga/{manga_id}/feed",
        params={"translatedLanguage[]": "en"},
    )

    for chapter in r.json()["data"]:
        if chapter_index in chapter['attributes']['chapter']:
            return chapter['id']

    return None 
