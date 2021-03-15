question=["how many continentes are there?","what is the copital of india","ng mai kon se course padhaye jate hai?"]
option=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software","counseting","tourism","agriculture"]]
solution=[3,4,1]
i=0
elist=[]
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j+=1
    a=int(input("enter the nas="))
    if a==solution[i]:
        elist.append(a)
    else:
        print("galat javab aap ka game finish")
    i+=1
print(elist)