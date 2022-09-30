# Library imports
import json
import os
import sys
from typing import List

# Local imports
from utils import *

def store_mangas_locally(storage_filename: str, mangas: List[Manga]) -> None:
    json_mangas = json.dumps([manga.get_dict() for manga in mangas], indent=4)
    with open(storage_filename, 'w') as storage:
        storage.write(json_mangas)

def read_local_storage(storage_filename: str) -> List[Manga]:
    with open(storage_filename) as storage:
        data = json.load(storage)
    return [Manga.parse_from_storage(raw) for raw in data]

def validate_file(filename: str) -> bool:
    return os.path.exists(filename) and os.path.getsize(filename) > 0

def get_name() -> str:
    with open('name.json') as preset:
        name = json.load(preset)['name']
    return name

def main() -> None:
    '''
    Main function
    '''
    if not args.title: return
    title    = ' '.join(arg.capitalize() for arg in args.title)
    fuzzy    = args.fuzzy
    search   = args.search
    site     = args.site
    chapter  = args.chapter
    refresh  = args.refresh
    english  = args.english
    language = 'english' if english else 'romaji'
    
    if search:
        redirect_search(title, site)
        sys.exit(0)

    name_filename = 'name.json'
    if not validate_file(name_filename):
        print('No name given, exiting..')
        return

    profile_name = get_name()

    # if there is no local storage, refresh and create a list of manga, also store the list
    storage_filename = 'stored.json'
    if refresh or not validate_file(storage_filename): 
        manga_list = refresh_mangas(profile_name) # refresh_manga, store manga, create_manga_list
        store_mangas_locally(storage_filename, manga_list)
    else:
        manga_list = read_local_storage(storage_filename)

    manga = get_manga(title, manga_list, fuzzy)
    if manga is None:
        print(f'Manga "{title}" not found!')
        return
    # get the redirection information and redirect
    redirection_info = get_redirect_info(manga, chapter, language, site)
    if redirection_info['title'] is None:
        print(f'Sorry, the manga "{title}" does not have an available title in "{language}"!')
        return

    redirect(redirection_info)
    sys.exit(0)

if __name__ == '__main__':
    main()
