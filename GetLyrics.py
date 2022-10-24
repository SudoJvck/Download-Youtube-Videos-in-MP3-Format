#Install LyricsGenius Library before Building
#Need API key from Genius.com/api-clients

import lyricsgenius
api_key = "arbdR_jDv_sB3phNTGQynMEiY7myq8DW5TquR7HMpRFtcVhl96bhnKxGWKeTGnl6"
genius = lyricsgenius.Genius(api_key)
name = input("Enter Artist Name : ")
artist = genius.search_artist(name, max_songs=3)
song = input("Type your song for Lyrics : ")
song = artist.song(song)
print(song.lyrics)
