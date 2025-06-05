import random

genres = {
    "rock": ["Led Zeppelin - Stairway to Heaven", "Queen - Bohemian Rhapsody", "The Rolling Stones - Paint It Black"],
    "pop": ["Taylor Swift - Shake It Off", "Dua Lipa - Don't Start Now", "Ariana Grande - 7 rings"],
    "hip-hop": ["Kendrick Lamar - HUMBLE.", "Drake - God's Plan", "Cardi B - I Like It"],
    "jazz": ["Miles Davis - So What", "John Coltrane - Giant Steps", "Ella Fitzgerald - Summertime"],
}

choice = input(
    "what genre of music do you like? (rock,pop,hip-hop,jazz): ").lower()

if choice in genres:
    print(
        f"Here are some {random.choice(genres[choice])}, songs you might like:")
else:
    print("☹ Sorry, I don't know that genre.")
