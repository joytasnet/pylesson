li=[]
li.append(int(input('国語>>')))
li.append(int(input('算数>>')))
li.append(int(input('理科>>')))
li.append(int(input('社会>>')))
li.append(int(input('英語>>')))
print(f'合計点{sum(li)},平均点{sum(li)/len(li)}')
