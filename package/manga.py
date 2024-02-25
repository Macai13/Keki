from collections.abc import Mapping
import requests
import mangadex

def get_manga(manga_title: str):
    api = mangadex.Api()

    manga_list = api.get_manga_list(title=manga_title)
    manga_id = manga_list[0].manga_id

    try:    
        manga = api.get_manga_volumes_and_chapters(manga_id = manga_id)

        return manga
    except TypeError as e:
        print(f"Manga not found\n{e}")

    return None


def get_chapter(volume_index: str, chapter_index: str, manga_dict):
    pass

#chapter_id = manga['50']['chapters']['491']['id']
