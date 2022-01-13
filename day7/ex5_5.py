def int_input(msg):
    return int(input(msg))

def calc_payment(amount,people=2):
    dnum=amount/people
    pay=dnum//100*100
    if dnum > pay:
        pay=int(pay+100)
    payorg=amount-pay*(people-1)
    return pay,payorg

def show_payment(pay,payorg,people=2):
    print('***支払額***')
    print(f'1人あたり{pay}円({people-1}人),幹事は{payorg}円です')

# 計算データの入力
amount=int_input('支払総額を入力してください')
people=int_input('参加人数を入力してください')

#割り勘の計算
pay,payorg=calc_payment(amount,people)

#結果の表示
show_payment(pay,payorg,people)
