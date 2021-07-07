def isvo(s):
    if s=="A" or s=="E" or s=="I" or s=="O" or s=="U":
        return True
    return False    

def minion_game(string):
    # your code goes here
    st=0
    ke=0
    for i in range(len(string)):
        if isvo(string[i])==True:
            ke+=len(string)-i
        else:
            st+=len(string)-i    

    if ke>st:
        print("Kevin",ke)
    elif st>ke:
        print("Stuart",st)
    else:
        print("Draw")    
if __name__ == '__main__':
    k=str(input())
    minion_game(k)