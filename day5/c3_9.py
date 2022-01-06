score = int(input('試験の点数を入力してください>>'))
if score < 0 or score > 100:
    print('異常な得点です')
elif score >= 60:
    print('合格!')
    print('よく頑張りました')
else:
    print('残念ながら不合格です')
    print('追試を受けてください')
