question=["how many continents are there?","what is the copitial of india?","NG mai kon se course padhaye jate hai"]
option=[["fore","nine","eight","seven"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling","tourism","agriculture"]]
solution=[3,4,1]
i=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j+=1
    a=int(input("enter the ans="))
    if a==solution[i]:
        print("congrachulation,answer is correct")
    else:
        print("wrong")
    i+=1
