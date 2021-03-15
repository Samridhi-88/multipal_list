question=["how many continents are there?","what is the captal of india","NG mai kon se cours padhaye jate hai?"]
option=[["fore","nine","seven","eight"],["chandigarh","bhopal","chennai","delhi"],["software engineering","counseling","tourism","agriculture"]]
i=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j+=1
    print()
    i+=1