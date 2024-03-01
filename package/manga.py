import mangadex
import requests
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QPixmap

API = mangadex.Api()
title: str = ''

def get_manga(manga_title: str):    
    global title
    
    manga_list = API.get_manga_list(title=manga_title)
    manga_id = manga_list[0].manga_id
    title = manga_list[0].title["en"]

    return manga_id


def get_chapter_id(chapter_index: str, manga_id: str, lang: str):
    base_url = "https://api.mangadex.org"

    r = requests.get(
        f"{base_url}/manga/{manga_id}/feed",
        params={"translatedLanguage[]": f"{lang}"},
    )

    for chapter in r.json()["data"]:
        if chapter_index == chapter["attributes"]["chapter"]:
            return (chapter["id"], title)

    return None, title


def get_chapter(chapter_id: str):
    return API.get_chapter(chapter_id=chapter_id).fetch_chapter_images()


def get_page(url: str):
    img = Image.open(requests.get(url, stream=True).raw)
    img = img.resize(size=(520, 780), resample=Image.Resampling.BICUBIC)

    qim = ImageQt(img)
    pixmap = QPixmap.fromImage(qim)
    pixmap.detach()

    return pixmap
