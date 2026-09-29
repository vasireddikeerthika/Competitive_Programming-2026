n = input()
pre = ''
for i in range(len(n)):
    pre += n[i]
    if (pre * (len(n)//len(pre))) == n:
        print(len(pre))
        break
