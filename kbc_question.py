question_list=["how many continents are there?","what is the capital of india?","NG me kon se cours padhaye jate hai?"]
option_list=[["fore","nine","seven","eight"],["chandigharh","bhopal","chennai","delhi",],["software engineering","counseling","tourism","agriculture"]]
solution=[3,4,1]
i=0
while i<len(question_list):
    print("Q",i+1,question_list[i])
    j=0
    while j<len(option_list[i]):
        print(j+1,option_list[i][j])
        j=j+1
    a=int(input("ans="))
    if a==solution[i]:
        print("congrachulation,answer is correct")
    else:
        print("wrong")
    i+=1
