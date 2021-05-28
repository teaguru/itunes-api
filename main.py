import itunespy
#kind, collectionName, trackName, collectionPrice, trackPrice, primaryGenreName, trackCount, trackNumber, releaseDate.
artist = itunespy.search_artist('The Beatles')  # Returns a list
albums = artist[0].get_albums()  # Get albums from the first result

for album in albums:
    print("==============albumname==============")
    print(album.collection_name, album.primaryGenreName, album.track_count, album.release_date, album.collection_id)
    print(album)
    print("vvvvv----------------album------------vvvvv")


    album = (itunespy.search_album(album.collection_name))
    print(album)# Returns a list
    tracks = album[0].get_tracks()  # Get tracks from the first result

    for track in tracks:
      print( track.artist_name + ': '+ track.track_name + str(track.get_track_time_minutes()) + " price " + str(track.track_price) + str(track.kind) + str())
      print('Total playing time: ' + str(album[0].get_album_time()))
