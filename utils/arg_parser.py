import argparse as ap

parser = ap.ArgumentParser(prog='Manga redirect' , description='A script that redirects you to your specified manga')

# --Available arguments--
# -r/--refresh: refreshing stored local database of mangas.
parser.add_argument('-r', '--refresh', action='store_true', help='refresh the contents of the local database')

# -c/--chapter: read a specific chapter, defaults to -1.
parser.add_argument('-c', '--chapter', type=int, default=-1, metavar='<chapter>', help='read specific chapter')

# -S, --search: search for a manga insead of going to the specific chapter
parser.add_argument('-S', '--search', default=False, action='store_true', help='search for manga')

# --Exact/fuzzy-ish--
# Add option to search exact or a bit fuzzy
parser.add_argument('-f', '--fuzzy', default=False, action='store_true', help='fuzzy-ish search')

# --Sites--
# Option to specify which site you want to read on
parser.add_argument('-s', '--site', type=str, metavar='<site>', default='mangasee', choices=['mangasee', 'mangapanda', 'mangafreak'])

# --Languages--
# These options are defined to have alternatives if something with the redirection goes wrong.
# -E/--english
parser.add_argument('-E', '--english', default=False, action='store_true')

# -R/--romaji
parser.add_argument('-R', '--romaji', default=True, action='store_true')

# title (positional): the title of the manga you want to read. It is stored as an array.
parser.add_argument('title', type=str, nargs='*', help='title of manga to read')
args = parser.parse_args()
