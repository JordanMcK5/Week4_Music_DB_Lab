from db.run_sql import run_sql
from models.albums import Albums
# from models.artists import Artists
# from repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Albums(result['title'], result['genre'], result['artist'])
    return album

def select_all():  
    albums = [] 
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for result in results:
        album = Albums(result['title'], result['genre'], result['artist'])
        albums.append(album)
    return albums 