def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))

eat(breakfast='納豆ご飯',lunch='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ごはん')
eat('納豆ご飯',dinner='カレーうどん')

print('hello','world',end='',sep=',')
