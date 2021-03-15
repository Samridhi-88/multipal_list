n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
dupli=[]
while i<len(n):
    if n[i] not in dupli:
        dupli.append(n[i])
    i+=1
print(dupli)



"""n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
dupal=[]
count=0
while i<len(n):
    j=0
    while j<len(n):
        count=0
        if n[i]==n[j]:
            count+=1
            if count>1:
                a.append(n[i])
        
    j+=1
print(dupal)"""