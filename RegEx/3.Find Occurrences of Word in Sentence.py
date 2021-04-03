import re

text = input().lower()
wanted_word = input().lower()

pattern = f"\\b{wanted_word}\\b"

result = re.findall(pattern, text)

print(len(result))