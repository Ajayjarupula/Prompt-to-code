import random

song_data = {
    "Dance/Party": [
        {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars"},
        {"title": "Shape of you", "artist": "Ed Sheeran"},
        {"title": "Party Rock Anthem", "artist": "MFAO"}
    ],
    "Calm": [
        {"title": "Weightless", "artist": "Marconi Union"},
        {"title": "Clair de Lune", "artist": "Claude Debussy"},
        {"title": "Sunrise", "artist": "Norah Jones"}
    ],
    "Lo-fi":[
        {"title": "Lofi Hip-Hop Beats", "artist": "Various Artists"},
        {"title": "Night Owl", "artist": "Jinsang"},
        {"title": "Lofi Chillhop", "artist": "DJ Grumble"}
    ],
    "Acoustic":[
        {"title": "Banana Pancakes", "artist": "Jack Johnson"},
        {"title": "The A Team", "artist": "Ed Sheeran"},
        {"title": "I'm Yours", "artist": "Jason Mraz"}
    ]
}

def get_song_recommendation(mood):
    if mood not in song_data:
        return "Sorry, we don't have songs for that mood at the moment."

    songs = song_data[mood]
    recommendations = random.sample(songs, 3)
    return recommendations

def show_popular_playlists():
    print("Popular Playlists:")
    for mood in song_data.keys():
        print(f"- {mood}")

def recommend_songs_for_mood():
    print("Please select a mood or occasion:")
    show_popular_playlists()

    selected_mood = input("Enter the mood (e.g., Dance/Party, Calm, Slow, Lo-fi, Acoustic): ").strip()
    recommendation = get_song_recommendation(selected_mood)

    if isinstance(recommendation, str):
        print(recommendation)
    else:
        print(f"Recommended Songs for {selected_mood}:")
        for song in recommendation:
            print(f"{song['title']} by {song['artist']}")

if __name__ == "__main__":
    recommend_songs_for_mood()