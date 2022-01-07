def eat(breakfast,lunch,dinner='カレー',*desserts):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(lunch))
    print('夜は{}を食べました'.format(dinner))

    for d in desserts:
        print('おやつに{}をたべました'.format(d))

eat('トースト','ぱすた','カレー','アイス','チョコ','カレー')
