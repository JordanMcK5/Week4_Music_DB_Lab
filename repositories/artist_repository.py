from db.run_sql import run_sql
from models.artists import Artists
# from models.albums import Albums
# from repositories.albums_repository as albums_repository

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artists(result['name'])
    return artist

def select_all():  
    artists = [] 
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for result in results:
        artist = Artists(result['name'])
        artists.append(artist)
    return artists 