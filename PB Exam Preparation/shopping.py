budget = float(input())
video_cards = int(input())
processors = int(input())
memory = int(input())

total_video_cards = video_cards * 250
price_processors = total_video_cards * 0.35
total_processors = price_processors * processors
price_memory = total_video_cards * 0.1
total_memory = price_memory * memory

total = total_video_cards + total_processors + total_memory

if video_cards > processors:
    total = total - (total * 0.15)

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")