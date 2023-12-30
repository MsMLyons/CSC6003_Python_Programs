""" 
File: lyonsm_module_6.py
Author: Marki Lyons
Course: Foundations in Programming Fall 2023
Module: 6
Date Created: 2023-11-25
Date Updated: 2023-12-05

Description: This program makes use of a dictionary to store a
collection of song titles and their corresponding artists. The
user is prompted to input a song title and an artist. They are
then prompted to update and delete songs of their choosing.
Finally, the program displays all songs entered by the user.
"""
# needs a menu to allow for user selection of operations
class Music_Collection:
    """ This class houses the functions that allow for the creation of a music collection """
    def __init__(self):
        """ Function to initialize an empty dictionary to hold the collection """        
        self.music_collection = {}

    def add_song(self):
        """ Function to add songs to the collection via user input """
        response = int(input("\nYou may enter up to 5 songs. How many would you like to enter? ")) 
        if 1 <= response <= 5:
            for num in range(response):
                title = input("\nPlease enter the title of a song: ").strip().lower()
                artist = input("\nPlease enter the artist who performs that song: ").strip().lower()
                self.music_collection[title] = artist
                print(f"\n{title.title()} by {artist.title()} is now part of the music collection.")            
        else: 
            print("\nSorry, invalid number. Please enter a number between 1 and 5.")
            exit()

    def get_song(self):
        """ Function to retrieve a song based on its title """
        response = input("\nWould you like to retrieve a song? (y/n): ").strip().lower()
        if response == "y":
            title = input("\nPlease enter the title of the song you'd like to retrieve from the collection: ").strip().lower()
            artist = self.music_collection.get(title, None)
            if artist is None:
                print("\nThat song is not in the music collection.")
            else: 
                print(f"\nGreat song! {title.title()} is by {artist.title()}")
            return artist
        elif response == "n":
            print("\nOk. Come back later to add more songs. Goodbye!")
            exit()
        else:
            print("\nSorry. Cannot retrieve a song without valid input.")
    
    def update_song(self):
        """ Function to update a song based on its title """
        response = input("\nWould you like to update a song? (y/n): ").strip().lower()
        if response == "y":
            title = input("\nPlease enter the title of the song you'd like to update: ").strip().lower()
            if title in self.music_collection:
                new_artist = input("\nPlease enter the artist's name: ").strip().lower()
                self.music_collection[title] = new_artist
                print(f"\n{title.title()} has been updated with the new artist: {new_artist.title()}")
            else: 
                print("\nThat song isn't part of the collection.")
        else:
            print("\nSorry. Invalid input. Cannot retrieve a song for updating.")

    def delete_song(self):
        """ Function to delete a song based on its title """
        response = input("\nWould you like to delete a song from the music collection? (y/n): ").strip().lower()
        if response == "y":
            title = input("\nPlease enter a song to delete: ").strip().lower()
            if title in self.music_collection:
                del self.music_collection[title]
                print(f"\n{title.title()} has been removed from the collection.")
            else:
                print("\nThat song isn't part of the collection.") 
        else:
            print("\nSorry. Invalid input. Cannot retrieve a song for deleting.")       

    def display_collection(self):
        """ Function to display all songs """
        if not self.music_collection:
            print("\nThere are currently no songs in the music collection. Goodbye!")
        else:        
            print("\nThese are the songs in the music collection: \n")
            for title, artist in self.music_collection.items():
                print(f"**{title.title()} by {artist.title()}")


def main():    
    collection = Music_Collection()

    print("\nWelcome to the music collection!")
    print("\nThere are currently no songs in the music collection.")
    print("\nThat's sad. Let's add some.")

    collection.add_song()

    collection.get_song()

    collection.update_song()

    collection.delete_song()

    collection.display_collection()
main()