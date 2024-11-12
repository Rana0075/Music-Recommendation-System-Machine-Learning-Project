import mysql.connector as mysql
import json

# Load the mood_genre_artist data
with open("mood_genre_artist.txt", "r", encoding="utf-8") as data:
    mood_genre_artist = json.load(data)

with open("artist_genre_album.txt", "r", encoding="utf-8") as data:
    artist_genre_album = json.load(data)

# Set up MySQL connection
conn = mysql.connect(
    host="localhost",  # replace with your host
    user="root",  # replace with your username
    password="root",  # replace with your password
    database="music_recommendation_system"
)

cursor = conn.cursor()

# Insert genres into genre_table


# for mood_name, genres in mood_genre_artist.items():
#     # First, get the mood_id for the current mood_name
#     cursor.execute("SELECT mood_id FROM mood_table WHERE mood_name = %s", (mood_name,))
#     mood_id = cursor.fetchone()[0]  # Retrieve the mood_id
    
#     # Insert genres for the current mood
#     for genre_name in genres.keys():
#         cursor.execute(
#             "INSERT INTO genre_table (genre_name, mood_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE genre_name=genre_name",
#             (genre_name, mood_id)
#         )


# for mood_name, genres in mood_genre_artist.items():
#     for genre_name, artists in genres.items():
#         # Get the genre_id for the current genre_name
#         cursor.execute("SELECT genre_id FROM genre_table WHERE genre_name = %s", (genre_name,))
#         genre_id = cursor.fetchone()[0]  # Retrieve the genre_id
        
#         # Insert artists for the current genre
#         for artist_name in artists:
#             cursor.execute(
#                 "INSERT INTO artist_table (artist_name, genre_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE artist_name=artist_name",
#                 (artist_name, genre_id)
#             )
for artist_name, albums in artist_genre_album.items():
    # Get the artist_id for the current artist_name
    cursor.execute("SELECT artist_id FROM artist_table WHERE artist_name = %s", (artist_name,))
    artist_id_result = cursor.fetchone()
    
    # Check if artist_id was found
    if artist_id_result is not None:
        artist_id = artist_id_result[0]  # Retrieve the artist_id
        
        # Insert albums for the current artist
        for album_name in albums:
            cursor.execute(
                "INSERT INTO album_table (album_name, artist_id) VALUES (%s, %s)",
                (album_name, artist_id)
            )
        
    else:
        print(f"Artist '{artist_name}' not found in artist_table.")
    
# Commit to ensure data is inserted
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

#print("Albums successfully inserted into the album_table.")

# print("Artists successfully inserted into the artist_table.")

# print("Moods successfully inserted into the mood_table.")

# print("Genres successfully inserted into the genre_table.")