percent = int(input())

def loading_bar(per):
    if percent == 10:
        print("10% [%.........]")
        print("Still loading...")
    elif percent == 20:
        print("20% [%%........]")
        print("Still loading...")
    elif percent == 30:
        print("30% [%%%.......]")
        print("Still loading...")
    elif percent == 40:
        print("40% [%%%%......]")
        print("Still loading...")
    elif percent == 50:
        print("50% [%%%%%.....]")
        print("Still loading...")
    elif percent == 60:
        print("60% [%%%%%%....]")
        print("Still loading...")
    elif percent == 70:
        print("70% [%%%%%%%...]")
        print("Still loading...")
    elif percent == 80:
        print("80% [%%%%%%%%..]")
        print("Still loading...")
    elif percent == 90:
        print("90% [%%%%%%%%%.]")
        print("Still loading...")
    elif percent == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")

loading_bar(percent)
