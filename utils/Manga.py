from __future__ import annotations
from typing import NamedTuple, Optional, List, Dict, Any

from .Types import JSONtype

class Manga(NamedTuple):
    '''
    Tuple to store information about a manga
    '''
    progress : int
    chapters : Optional[int]
    titles   : Dict[str, Optional[str]]

    def get_dict(self) -> Dict[str, Any]:
        return {
            'progress' : self.progress,
            'chapters' : self.chapters,
            'titles'   : self.titles
        }

    def get_titles(self) -> List[str]:
        return [v for v in self.titles.values() if v] 

    @staticmethod
    def parse_from_storage(raw: Manga) -> Manga:
        progress = raw['progress']
        chapters = raw['chapters']
        titles = raw['titles']
        return Manga(progress, chapters, titles)

    @staticmethod
    def parse_manga(raw: JSONtype) -> Manga:
        '''
        Parse an individual manga entry
        '''
        progress = int(raw['progress'])
        media = raw['media']
        chapters = int(c) if (c:=media['chapters']) else None
        media_titles = media['title']
        format_title = lambda title: ' '.join(word.capitalize() for word in title.split() if word)
        titles = {
            'romaji'  : format_title(t) if (t:=media_titles['romaji' ]) is not None else None,
            'english' : format_title(t) if (t:=media_titles['english']) is not None else None
        }
        return Manga(progress, chapters, titles)

    @staticmethod
    def manga_list_from_api(raw: Any) -> List[Manga]:
        '''
        Return a list of parsed Manga instances
        '''
        manga_list: List[Manga]=[]
        data  = raw['data']
        mlc   = data['MediaListCollection']
        lists = mlc['lists']
        for m_list in lists:
            entries = m_list['entries']
            for entry in entries:
                manga_list.append(Manga.parse_manga(entry))
        return manga_list
