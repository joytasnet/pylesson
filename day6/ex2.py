def min_max(n,*args):
    ls=list(args)
    ls.append(n)
    return max(ls),min(ls)

maxN,minN = min_max(3,4,1,5,3)
print(f'最大{maxN},最小{minN}')
