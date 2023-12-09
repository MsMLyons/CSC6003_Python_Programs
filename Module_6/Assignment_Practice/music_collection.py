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
    def __init__(self):        
        self.music_collection = {}

    def add_song(self):       
        title = input("\nPlease enter the title of a song: ")
        artist = input("\nPlease enter the artist who performs that song: ")
        self.music_collection[title] = artist
        print(f"\n{title.title()} by {artist.title()} is now part of the music collection.")

    def get_song(self):
        title = input("\nPlease enter the title of the song you'd like to retrieve from the collection: ").strip()
        artist = self.music_collection.get(title, "\nThat song isn't part of the collection.")
        print(f"\n{title.title()} is by {artist.title()}")
        return artist
    
    def update_song(self):
        title = input("\nPlease enter the title of the song you'd like to update: ").strip()
        new_artist = input("\nPlease enter the artist's name: ").strip()
        self.music_collection[title] = new_artist
        print(f"\n{title.title()} has been updated with the new artist: {new_artist.title()}")

    def delete_song(self):
        response = input("\nWould you like to delete a song from the music collection? (y/n): ").strip().lower()
        if response == "y":
            title = input("\nPlease enter a song to delete: ").strip()
            if title in self.music_collection:
                del self.music_collection[title]
                print(f"\n{title.title()} has been removed from the collection.")
            else:
                print("\nThat song isn't part of the collection.")
        # else:
        #     self.add_song()

    def display_collection(self):        
        if not self.music_collection:
            print("\nThere are currently no songs in the music collection.")
            print("\nThat's sad. Let's add some.")
            self.add_song()
        else:
            print("\nThese are the songs in the music collection: \n")

            # songs_to_add = []

            for title, artist in self.music_collection.items():
                print(f"{title.title()} by {artist.title()}")
            #     response = input("\nWant to add more songs to the music collection? (y/n): ").strip().lower()
            #     if response == "y":
            #         songs_to_add.append((title, artist))
            #     else:
            #         print("\nOk. Maybe another day. Goodbye!")

            # for title, artist in songs_to_add:
            #     self.music_collection[title] = artist                


collection = Music_Collection()
print("\nWelcome to the music collection!")


collection.display_collection()

collection.add_song()

collection.update_song()

collection.delete_song()

collection.display_collection()