question=["how many continentes are there?","what is the copital of india","ng mai kon se course padhaye jate hai?"]
option=[["four","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software","counseting","tourism","agriculture"]]

fiftyfifty=[["four","seven"],["delhi","bhopal",],["tourism","software engineering"]]
solution=[3,4,1]
sol=[2,1,2]
i=0
c=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j+=1
    a=int(input("answer="))
    if a==solution[i]:
        print("congrats")
    elif a==5050:
        if c==0:
            m=0
            while m<len(fiftyfifty[i]):
                print(m+1,fiftyfifty[i][m])
                m=m+1
            c=c+1
            num=int(input("enter the num"))
            if num==solution[i]:
                print("correct")
            else:
                print("your option is wrong")
                break
        else:
            print("you used 5050 lifeline")
            num1=int(input("enter the option"))
            if num1==solution[i]:
                print("congrats")
            else:
                print("your option is wrong")
                break
    else:
        print("your answer is wrong")
        break
    i+=1
