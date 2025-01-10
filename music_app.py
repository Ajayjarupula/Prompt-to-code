import pandas as pd

class MusicDatabase:
    def __init__(self, data):
        #Initialize with a list of dictionaries(Songs Data)
        self.songs = pd.DataFrame(data)

    def search_songs(self, language=None, artist=None, region=None, country=None, genre=None, album=None, min_duration=None, max_duration=None, release_date=None):
        #Apply filters based on user inputs
        filtered_songs = self.songs

        if language:
            filtered_songs = filtered_songs[filtered_songs['language'] == language]
        if artist:
            filtered_songs = filtered_songs[filtered_songs['artist'].str.contains(artist, case=False)]
        if region:
            filtered_songs = filtered_songs[filtered_songs['region'] == region]
        if country:
            filtered_songs = filtered_songs[filtered_songs['country'] == country]
        if genre:
            filtered_songs = filtered_songs[filtered_songs['genre'] == genre]
        if album:
            filtered_songs = filtered_songs[filtered_songs['album'].str.contains(album, case=False)]
        if min_duration:
            filtered_songs = filtered_songs[filtered_songs['duration'] >=min_duration]
        if max_duration:
            filtered_songs = filtered_songs[filtered_songs['duration'] >=max_duration]
        if release_date:
            filtered_songs = filtered_songs[filtered_songs['release_date'] >= release_date]

        return filtered_songs
    



songs_data = [
    {'song_id': 1, 'song_title': 'Song A', 'language': 'English', 'artist': 'Artist X', 'region': 'North America', 'country': 'USA', 'genre': 'Pop', 'album': 'Album 1', 'duration': 240, 'release_date': '2020-05-01'},
    {'song_id': 2, 'song_title': 'Song B', 'language': 'Spanish', 'artist': 'Artist Y', 'region': 'South America', 'country': 'Argentina', 'genre': 'Rock', 'album': 'Album 2', 'duration':180, 'release_date': '2019-06-15'},
    {'song_id': 3, 'song_title': 'Song C', 'language': 'English', 'artist': 'Artist X', 'region': 'North America', 'country': 'Canada', 'genre': 'Pop', 'album': 'Album 1', 'duration': 210, 'release_date': '2021-01-10'},
    {'song_id': 4, 'song_title': 'Song D', 'language': 'Hindi', 'artist': 'Artist Z', 'region': 'Asia', 'country': 'India', 'genre': 'Classical', 'album': 'Album 3', 'duration': 300, 'release_date': '2022-12-01'},
]


music_db = MusicDatabase(songs_data)

search_result = music_db.search_songs(artist='Artist z', language='Hindi')
print(search_result)