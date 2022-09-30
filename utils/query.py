query = '''query($name: String){
  MediaListCollection(userName: $name, type: MANGA){
    lists {
      entries {
        progress
        media {
          chapters
          title {
            romaji
            english
          }
        }
      }
    }
  }
}'''
