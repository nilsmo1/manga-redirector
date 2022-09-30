import requests   as rq
import webbrowser as wb
from typing import Optional, List, Union

from .Manga import Manga
from .query import query
from .Types import RedirectInfo
from .urls  import ANILIST_API_URL, SITE_URLS, SITE_TITLE_FORMATS, SITE_SEARCH_URLS, SITE_SEARCH_FORMATS

# --Helper functions--
def format_title(title: str) -> str:
    return ' '.join(word.capitalize() for word in title.split() if word) 

def get_correct_chapter(chapter: int, progress: int) -> int:
    return progress+1 if chapter < 0 else chapter

def get_manga(title: str, manga_list: List[Manga], fuzzy: bool) -> Optional[Manga]:
    if not fuzzy:
        for manga in manga_list:
            if format(title) in manga.get_titles():
                return manga
        return None
    for manga in manga_list:
        for lang in manga.get_titles():
            if format(title) in lang:
                return manga
    return None

def create_url(title: str, chapter: int, site: str) -> str:
    f_title = SITE_TITLE_FORMATS[site](title)
    return SITE_URLS[site](f_title, chapter)

def create_search_url(title: str, site: str) -> str:
    f_title = SITE_SEARCH_FORMATS[site](title)
    return SITE_SEARCH_URLS[site](f_title)

def refresh_mangas(name: str) -> List[Manga]:
    variables = {'name': name}
    response = rq.post(ANILIST_API_URL, json={'query': query, 'variables': variables})
    json_response = response.json()
    manga_list = Manga.manga_list_from_api(json_response)
    return manga_list

def get_redirect_info(manga: Manga, chapter: int, language: str, site: str) -> RedirectInfo:
    title = manga.titles[language]
    progress = manga.progress
    correct_chapter = get_correct_chapter(chapter, progress)
    return {
        'title'   : title,
        'chapter' : correct_chapter,
        'site'    : site
    }

def redirect_search(title: str, site: str) -> None:
    url = create_search_url(title, site)
    print(f'''SEARCH:\n\t{url=}\n\t{title=}\n\t{site=}''')
    wb.open(url) 


def redirect(info: RedirectInfo) -> None:
    site     = info['site']
    title    = info['title']
    chapter  = info['chapter']
    url = create_url(title, chapter, site)
    print(f'''READ:\n\t{url=}\n\t{title=}\n\t{chapter=}\n\t{site=}''')
    wb.open(url)
