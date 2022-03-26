print("###Quiz Start###")
    #Test
TotalQ=len(QList) 
QNum=1
AList=[]
while QNum<=TotalQ:

    print(QNum,". ",QList[QNum-1])
    print("Ans.: ")
    AList.append(input())
    QNum+=1
print("Finished!")

    #evalution
print("Now Evalute Your Quiz: \n  Q=Question, \n  YA=Your Answer \n  CA=Correct Answer. \n If your answer is Correct enter 1 , otherwise enter O")
Score=0
QNum=1
while QNum<=TotalQ:
    x=QNum-1
    y=QList[x]
    print("Q",QNum,": ",y)
    print("YA: ",AList[x])
    print("CA: ", QADict.get(y))
    print("Score?(1 or 0)")
    Score+=int(input())
    QNum+=1

print("You've got %d out of %d ." %(Score, TotalQ))
print("See ya!")