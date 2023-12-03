music_collection = {
    "Don't Eat My Tortilla Chips" : "Jack & Anita",
    "Why Not?": "The Little Kids",
    "Only a Snack" : "The Mighty Teens",
}

# access a value using a tuple key
musical_artist = music_collection[("Why Not?")]
print(f"\nThe song 'Why Not?' is sung by {musical_artist}.")

# output --> The song 'Why Not?' is sung by The Little Kids.

# iterate over the dictionary and print a list of the songs
print("\nThese are the songs in my music collection:\n")
for title, artist in music_collection.items():    
    print(f"{title} by {artist}\n")

# output --> 
    # These are the songs in my music collection:

    # Don't Eat My Tortilla Chips by Jack & Anita
    # Why Not? by The Little Kids
    # Only a Snack by The Mighty Teens

# update the music collection
music_collection.update({"Snacks After Dinner" : "Bruh"})
print(music_collection)

# output -->
    # {
    # "Don't Eat My Tortilla Chips": 'Jack & Anita', 
    # 'Why Not?': 'The Little Kids', 
    # 'Only a Snack': 'The Mighty Teens', 
    # 'Snacks After Dinner': 'Bruh'
    # }