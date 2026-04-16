import random

lotto = []

while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto: 
        lotto.append(num)

lotto.sort()
print(f"추첨된 로또 번호 ==>", end =" ")
for i in range(0, 6) :
  print(f"{lotto[i]}", end = " ")