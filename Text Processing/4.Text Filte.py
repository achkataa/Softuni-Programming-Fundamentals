ban = input().split(", ")
text = input()

for word in ban:
    if word in text:
        text = text.replace(word, len(word) * "*")

print(text)