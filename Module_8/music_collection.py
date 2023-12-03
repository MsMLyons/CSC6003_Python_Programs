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
    def __init__(self, title, artist):        
        self.title = title
        self.artist = artist

    def add_song(self):
        # add_song = Music_Collection.dict()        
        self.title = input("Please enter the title of a song: ")
        self.artist = input("Please enter the artist who performs that song: ")
        # add_song.append(self.title, self.artist)

        # for k, v in self.title.iteritems():
        #     print(k, v)

        # for k, v in self.artist.items():
        #     print(k, v)
        

# song1 = Music_Collection("dance dance", "never dance again") 
# print(f"My favorite song is {song1.title} by {song1.artist}.") 
new_song = Music_Collection.add_song()
        



