genres = input().split(" | ")

command = input()


def join(genres, genre):
    if genre not in genres:
        genres.append(genre)

def drop(genres, genre):
    if genre in genres:
        genres.remove(genre)

def replace(genres, old_genre, new_genre):
    if old_genre in genres and new_genre not in genres:
        old_genre_index = genres.index(old_genre)
        genres.remove(old_genre)
        genres.insert(old_genre_index, new_genre)

while command != "Stop!":
    data = command.split()
    action = data[0]

    if action == "Join":
        genre = data[1]
        join(genres, genre)
    elif action == "Drop":
        genre = data[1]
        drop(genres, genre)
    elif action == "Replace":
        old_genre = data[1]
        new_genre = data[2]
        replace(genres, old_genre, new_genre)

    command = input()

print(' '.join(genres))