import mangadex
import requests
import PIL
from PIL import Image
from io import BytesIO
from PIL.ImageQt import ImageQt
from PyQt6.QtGui import QPixmap

API = mangadex.Api()

def get_manga(manga_title: str):    
    manga_list = API.get_manga_list(title=manga_title)
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


def get_chapter(chapter_id: str):
    return API.get_chapter(chapter_id=chapter_id).fetch_chapter_images()


def get_page(url: str):
    print("0")

    img = Image.open(requests.get(url, stream=True).raw)
    img = img.resize(size=(520, 780), resample=Image.Resampling.BICUBIC)

    qim = ImageQt(img)
    pixmap = QPixmap.fromImage(qim)
    pixmap.detach()

    print("1")

    return pixmap