print("###Create QuiZ###")
#Create Dictionary
print("Wanna Create a Quiz? (Click 'Enter') or Type 'end' to exit: ")
EndCommand=input()
if EndCommand!="end":
    QADict={}
    QList=[]

    while EndCommand!="end":
        print("Question: ")
        QKey=input()
        QList.append(QKey)
        print("Answer: ")
        AValue=input()
        TempDict={QKey:AValue}
        print("Q:A ~ ", TempDict)
        QADict.update(TempDict)
        #QADict[QKey]=AValue
        print("Add anoter Question?(Clcik 'Enter' key) or Want to End ?(Type 'end' and Click Enter) ")
        EndCommand=input()
    print("Question list and Dictionary for Quiz creation: Successfull! ~ ~ \n ",QList, "\n", QADict)
    

    print("Enter Quiz File name with .py extention in end: ")
    QuizFName=input()
    
    Source=open("Simple quiz source.py", "r")
    
    Output=open(QuizFName,"a")
    print("QADict=",QADict,file=Output)
    print("QList=",QList,file=Output)
    for line in Source:
      Output.write(line)
    Source.close()
    Output.close()
    
else:
    print("See ya!")