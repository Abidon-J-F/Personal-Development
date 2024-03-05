""" 
This is an User Albums program. Python3 creation.
Author: Abidon Jude Fernandes
Date: 07/2022 - 08/2022
"""

def make_album(artist_name, artist_title, no_of_albums= None):
    """Return a dictionary of information about a album."""
    album_dictonary = {'artist name': artist_name.title(), 'artist title': artist_title.title()}
    if no_of_albums:
        album_dictonary['number of album'] = no_of_albums
    return album_dictonary

while True:
    print("\nPlease tell me your Artist name:")
    print("(enter 'q' at any time to quit)")
    
    a_name = input("Artist Name: ")
    if a_name == 'q':
        break
    
    a_title = input("Artist Title: ")
    if a_title == 'q':
        break

    no_albums = input("Number of Albums: ")
    if no_albums == 'q':
        break

    album = make_album(a_name, a_title, no_albums)
    print(f"\n {album}!")