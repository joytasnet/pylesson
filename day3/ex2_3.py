hb1={'麻雀','自転車','映画','散歩','将棋'}
hb2={'麻雀','自転車','料理','ゲーム','読書'}
input('心の準備ができたらEnterキーを押してください')
print(f'二人の相性度は{len(hb1 & hb2) / len(hb1 | hb2) * 100}%です！')
