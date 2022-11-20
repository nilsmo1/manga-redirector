# manga-redirector-v2
Script that redirects you to a site where you can read a specified manga

Links to the APIs used:
[`AniList API`](https://anilist.gitbook.io/anilist-apiv2-docs/)
[`MangaDex API`](https://api.mangadex.org/docs/)

# Usage
Just clone, run `make install`, paste your AniList username into the `name.json` file, and everything should so
lve itself.
```bash
$ git clone git@github.com:nilsmo1/manga-redirector.git
$ cd manga-redirector/
$ make install
```
This will run the INSTALL script, which generates an executable, moves it to `~/.local/bin/`,
you then also have to insert your AniList `<username>` into the generated `name.json` file.
```json
{ "name": "<username>" } 
```
For help, run `manga-redirector -h/--help`.

