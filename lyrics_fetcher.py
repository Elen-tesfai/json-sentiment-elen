import lyricsgenius
import json
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve the Genius API Key from the environment variable
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")

if not GENIUS_API_KEY:
    print("Error: GENIUS_API_KEY not found in .env file.")
    exit()

def fetch_and_save_lyrics(artist, song, filename):
    # Initialize the Genius API client with the API key
    genius = lyricsgenius.Genius(GENIUS_API_KEY)
    
    # Set the Genius client to remove unnecessary data (for cleaner responses)
    genius.remove_section_headers = True

    try:
        # Search for the song and fetch lyrics
        song_info = genius.search_song(song, artist)
        
        # Print the raw response for debugging
        if song_info:
            print("Raw song data:", song_info)

        if song_info and song_info.lyrics:
            lyrics = song_info.lyrics
            data = {"artist": artist, "song": song, "lyrics": lyrics}
            
            # Write the lyrics to a file
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            print(f"Lyrics for '{song}' by {artist} saved to {filename}.")
        else:
            print(f"Song '{song}' by {artist} not found, or no lyrics available.")
    
    except Exception as e:
        print(f"Error occurred while fetching lyrics: {e}")

# Example usage
fetch_and_save_lyrics('They Might Be Giants', 'Birdhouse in Your Soul', 'birdhouse_in_your_soul.json')