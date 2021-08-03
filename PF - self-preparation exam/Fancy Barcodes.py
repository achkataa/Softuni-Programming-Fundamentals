import re

n = int(input())

barcodes = [input() for i in range(n)]

pattern = r"@#+[A-Z][a-zA-Z\d{4,}]+[A-Z]@#+"


for barcode in barcodes:
    if re.findall(pattern, barcode):
        nums = [char for char in barcode if char.isdigit()]
        if nums:
            print(f"Product group: {''.join(nums)}")
        else:
            print(f"Product group: {'00'}")
    else:
        print("Invalid barcode")