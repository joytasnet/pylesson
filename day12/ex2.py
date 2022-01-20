import random
data=[random.randrange(1,10,2) for i in range(10)]
print(data)
if 7 in data:
    print(f'index{data.index(7)}に７はありました')
else:
    print('7はありませんでした')



