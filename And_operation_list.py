'''

Write a function that returns the bitwise AND of all integers between List M and
List N (Equal Length) , using RECURSION TECHNIQUE

SAMPLE INPUT - [2,4,1,5,1]
               [3,0,2,4,1]

SAMPLE OUTPUT - [2,0,0,4,1]                

'''

#PROGRAM

i = 0
Empty_List = []
def Bitwise_And():
    global Empty_List,i

    ls1 = [2,4,1,5,1]
    ls2 = [3,0,2,4,1]

    if i == min(len(ls1),len(ls2)):
        return 'stop'

    else :
        res = (ls1[i] & ls2[i])
    i += 1
    Empty_List.append(res)
    Bitwise_And()
    return Empty_List
print(Bitwise_And())
