def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
        print(L)
                
def newSort(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
        print(L)
            
test = [4,7,8,2,3,6,0,9,1,5]
#mySort(test)
print()
test2 = [4,7,8,2,3,6,0,9,1,5]
#newSort(test2)


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

print(search([0,1,2,3,4,5,6,7,8,9,10,11,12,13], 15))
print(search([0,1,2,3,4,5,6,7,8,9,10,11,12,13], 5))
print(newsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13], 15))
print(newsearch([0,1,2,3,4,5,6,7,8,9,10,11,12,13], 5))
print()
print(search([0,1,2], 15))
print(search([0,1,2], 2))
print(newsearch([0,1,2], 15))
print(newsearch([0,1,2], 2))

def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)