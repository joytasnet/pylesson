import random
data=[random.randint(0,9) for i in range(10)]
print(data)
for i in range(len(data)):
    if data[i]==7:
        print(f'index{i}に7はありました')
        break
else:
    print('7はありませんでした')
