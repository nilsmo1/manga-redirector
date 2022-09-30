from typing import Optional, TypedDict, Union, Dict

RedirectInfo = Dict[str, Union[str, int]]

class Titles(TypedDict):
    romaji  : str
    english : str

class Media(TypedDict):
    chapters : Optional[int]
    titles   : Titles

class JSONtype(TypedDict):
    progress : int
    media    : Media
