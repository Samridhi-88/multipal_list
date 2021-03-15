paise=[3000,600000,324990909,90990900,3000,5600000,690909090,31010101,530010,510,4100]
i=0
c1,c2,c3=0,0,0
while i<len(paise):
    if paise[i]>=10000000:
        c1+=1
        print(i,"crorepahi pati")
    elif paise[i]>=100000:
        c2+=1
        print(i,"lakhpati")
    else:
        c3+=1
        print(i,"dilwale")
    i+=1
print(c1,c2,c3)