
def checkContains(subWord,mainWord):

    for i in subWord:
        if i not in mainWord or subWord.count(i) > mainWord.count(i) :
            return False

    return True

def main():
    result=False
    firstWord,secondWord="",""
    while firstWord != "last" and secondWord != "last":
        print("Enter first Word")
        firstWord = input()   
        print("Enter first Word")
        secondWord = input() 
        if len(firstWord) <= len(secondWord):
            result = checkContains(firstWord,secondWord)
        else :
            result = checkContains(secondWord,firstWord)

        print("=>",result,"\n")
       
main()