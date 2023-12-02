""" 
Music Collection Organizer

Description: You have been tasked with creating a program to organize a music collection using a dictionary in Python. The program should provide the following functionality:

1. Add a song: Prompt the user to enter the song title and artist, and add it to the music collection.
2. Retrieve song details: Prompt the user to enter a song title, and display the corresponding artist from the music collection.
3. Update song details: Prompt the user to enter a song title, and update the artist information in the music collection.
4. Delete a song: Prompt the user to enter a song title, and remove the corresponding song from the music collection.
5. Display all songs: Display all songs in the music collection. 

"""

class Music_Collection:
    def __init__(self, genre, song_title, artist):
        self.genre = genre
        self.song_title = song_title
        self.artist = artist

song1 = Music_Collection("pop", "dance dance", "never dance again") 
print(f"My favorite music genre is {song1.genre}. \nMy favorite song is {song1.song_title} by {song1.artist}.")   
        



