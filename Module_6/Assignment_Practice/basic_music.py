music_collection = {
    "Don't Eat My Tortilla Chips" : "Jack & Anita",
    "Why Not?": "The Little Kids",
    "Only a Snack" : "The Mighty Teens",
}

print("\nThese are the songs in my music collection:\n")
for title, artist in music_collection.items():    
    print(f"{title} by {artist}")