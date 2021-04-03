import math
record_in_seconds = float(input())
distance_in_metres = float(input())
one_metre_climbing = float(input())

all_seconds_climbing = distance_in_metres * one_metre_climbing

all_time = math.floor((distance_in_metres / 50)) * 30

total_time = all_time + all_seconds_climbing


if record_in_seconds <= total_time:
    print(f"No! He was {total_time - record_in_seconds:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {total_time:.2f} seconds.")