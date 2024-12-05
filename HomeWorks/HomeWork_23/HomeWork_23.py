import sqlite3
from typing import List, Dict


conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()


class Genre:
    def __init__(self, genre_id: int, name: str):
        self.genre_id = genre_id
        self.name = name

    @classmethod
    def from_row(cls, row: tuple) -> 'Genre':
        return cls(genre_id=row[0], name=row[1])


class Album:
    def __init__(self, album_id: int, title: str, artist_id: int):
        self.album_id = album_id
        self.title = title
        self.artist_id = artist_id

    @classmethod
    def from_row(cls, row: tuple) -> 'Album':
        return cls(album_id=row[0], title=row[1], artist_id=row[2])


class Artist:
    def __init__(self, artist_id: int, name: str):
        self.artist_id = artist_id
        self.name = name

    @classmethod
    def from_row(cls, row: tuple) -> 'Artist':
        return cls(artist_id=row[0], name=row[1])


class Track:
    def __init__(self, track_id: int, name: str, genre_id: int, album_id: int, media_type_id: int):
        self.track_id = track_id
        self.name = name
        self.genre_id = genre_id
        self.album_id = album_id
        self.media_type_id = media_type_id

    @classmethod
    def from_row(cls, row: tuple) -> 'Track':
        return cls(track_id=row[0], name=row[1], genre_id=row[2], album_id=row[3], media_type_id=row[4])


def get_long_genre_names() -> Dict[int, str]:
    cursor.execute("SELECT GenreId, Name FROM Genre WHERE LENGTH(Name) > 8")
    rows = cursor.fetchall()

    genres = {row[0]: row[1] for row in rows}
    return genres


long_genres = get_long_genre_names()
print("Genres with names longer than 8 characters:", long_genres)


def get_album_titles() -> List[str]:
    cursor.execute("SELECT title FROM Album")
    rows = cursor.fetchall()

    album_titles = [row[0] for row in rows]
    return album_titles


album_titles = get_album_titles()
print("Album titles:", album_titles)


conn.close()
