""" 
This is an Album program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def make_album(artist_name, artist_title, no_of_album= None):
    """Return a dictionary of information about a album."""
    album_dictonary = {'artist name': artist_name.title(), 'artist title': artist_title.title()}
    if no_of_album:
        album_dictonary['number of album'] = no_of_album
    return album_dictonary

album = make_album('eminem', 'america', no_of_album=3)
print(album)

album2 = make_album('DMC5', 'devil trigger')
print(album2)