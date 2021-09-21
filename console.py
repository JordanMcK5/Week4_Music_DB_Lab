import pdb 
from models.artists import Artists
import repositories.artist_repository as artist_repository  
from models.albums import Albums
import repositories.album_repository as album_repository  

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artists("Oasis")
artist_repository.save(artist1)
artist2 = Artists("Metallica")
artist_repository.save(artist2)

album1 = Albums("Time Flies...1994-2009","Rock","Oasis")
album_repository.save(album1)
album2 = Albums("Load","Rock","Metallica")
album_repository.save(album2)

found_artist = artist_repository.select(artist1.id)
found_album = album_repository.select(album1.id)

selected_album = album_repository.select_all()
selected_artist = artist_repository.select_all()


pdb.set_trace()