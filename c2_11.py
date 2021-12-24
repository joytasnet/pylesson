a=[10,20,30,40,50]
#超基本
print(a[1:3]) #[20,30]
print(a[2:]) #[30,40,50]
print(a[:3]) #[10,20,30]

#負のインデックスについて
print(a[-1]) #indexには負の値が使え後ろからを意味する50
print(a[-2]) #40

print(a[-3:]) #[30,40,50]

#スライス時には範囲外でもエラーにならない
print(a[0:100]) #[10,20,30,40,50]
#print(a[100])  エラー


#以下の方法だとyとxは同じリストを指す
x=[100,200,300]
y=x;
x[0]=500
print(y[0])

#リストのコピー作成
x=[100,200,300]
y=x[:]
x[0] = 500
print(y[0]) # 100

#スライス時の第三引数(step)
a=[1,2,3,4,5,6,7,8,9]
print(a[1:7:2]) #[2,4,6]
print(a[5:2:-1]) #[6,5,4]
print(a[::-1]) #[9,8,.....1]配列のリバース

#文字列でも同様
s='Hello World'
s2=s[1:5]
print(s2) #ello
print(s[::-1]) #dlrow olleH
print(s[-1]) #d



