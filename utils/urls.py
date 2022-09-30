ANILIST_API_URL = 'https://graphql.anilist.co'
SITE_URLS = {
    'mangasee'   : lambda t, c: f'https://mangasee123.com/read-online/{t}-chapter-{c}.html',
    'mangapanda' : lambda t, c: f'http://mangapanda.in/{t}-chapter-{c}',
    'mangafreak' : lambda t, c: f'https://w13.mangafreak.net/Read1_{t}_{c}'
}
SITE_TITLE_FORMATS = {
    'mangasee'   : lambda t: '-'.join(c.capitalize() for c in t.split()),
    'mangapanda' : lambda t: '-'.join(c.lower()      for c in t.split()),
    'mangafreak' : lambda t: '_'.join(c.capitalize() for c in t.split())
}
SITE_SEARCH_URLS = {
    'mangasee'   : lambda t: f'https://mangasee123.com/search/?name={t}',
    'mangapanda' : lambda t: f'http://mangapanda.in/search?q={t}',
    'mangafreak' : lambda t: f'https://w13.mangafreak.net/Search/{t}'
}
SITE_SEARCH_FORMATS = {
    'mangasee'   : lambda t: '%20'.join(t.split()),
    'mangapanda' : lambda t: '+'.join(t.split()),
    'mangafreak' : lambda t: '%20'.join(t.split())
}
