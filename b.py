name = input("氏名：")
birthday = input("生年月日：")
parts = birthday.split("/")

year = int(parts[0])
month = int(parts[1])
day = int(parts[2])

count = 0

for character in name:
    if character.isalpha():
        count += 1
total = count + year + month + day
if total % 6 == 0:
    fortune = "大吉"
elif total % 3 == 0:
    fortune = "中吉"
elif total % 2 == 0:
    fortune = "吉"
else:
    fortune = "凶"

print(f"{name}さんの運勢: {fortune}")
