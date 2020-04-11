def printLines(l):
    for i in range(len(l)):
        print(l[i], end="->")
    print("\n")

def moveleft(r, c, x, Lines, line, arr):
    #move left
    line.append(arr[r][c])
    for i in range(x):
        c -= 1
        line.append(arr[r][c])
    Lines.append(line)
    return r,c
    
def moveright(r, c, x, Lines, line, arr):
    #move right
    line.append(arr[r][c])
    for i in range(x):
        c +=1
        line.append(arr[r][c])
    Lines.append(line)
    return r,c

def moveup(r, c, x, Lines, line, arr):
    #move up
    line.append(arr[r][c])
    for i in range(x):
        r -= 1
        line.append(arr[r][c])
    Lines.append(line)
    return r,c

def movedown(r, c, x, Lines, line, arr):
    #move Down
    line.append(arr[r][c])
    for i in range(x):
        r += 1
        line.append(arr[r][c])
    Lines.append(line)
    return r,c

def findPath(n):

    #intialising the 2-D Array
    arr = [[(j,i) for i in range(n)] for j in range(n)] 
    for row in arr:
        print(row)
    #Find the center element
    if n%2 == 0:
        mid = int(n/2)-1
    else:
        mid = int(n/2)
    print("\n")
    
    #List that holds all the lines
    Lines= []
    #first 4 Lines a same for all the cases
    # Line 1 
    Line1 = []
    Line1.append(arr[mid+1][mid-1])
    Line1.append(arr[mid][mid])
    Line1.append(arr[mid-1][mid+1])
    #Line 2
    Line2 = []
    Line2.append(arr[mid-1][mid+1])
    Line2.append(arr[mid][mid+1])
    Line2.append(arr[mid+1][mid+1])
    if mid+2 < n:
        Line2.append(arr[mid+2][mid+1])
    #Line 3
    Line3 = []
    if mid+2 < n:
        Line3.append(arr[mid+2][mid+1])
    Line3.append(arr[mid+1][mid])
    Line3.append(arr[mid][mid-1])
    if mid-2 >=0 :
        Line3.append(arr[mid-1][mid-2])
    #line 4
    Line4 = []
    if mid-2 >=0 :
        Line4.append(arr[mid-1][mid-2])
    Line4.append(arr[mid-1][mid-1])
    Line4.append(arr[mid-1][mid])
    Line4.append(arr[mid-1][mid+1])
    if mid+2 < n:
        Line4.append(arr[mid-1][mid+2])

    Lines.append(Line1)
    Lines.append(Line2)
    Lines.append(Line3)
    Lines.append(Line4)

    if n == 4 :
        line = []
        r = mid - 1
        c = mid + 2 
        r, c = movedown(r, c, 3, Lines, line, arr)
        line = []
        r,c = moveleft(r, c, 3, Lines, line, arr)
    if n > 4:
        Line5 = []
        for i in range(0,4):
            Line5.append(arr[mid-1+i][mid+2]) 
        Lines.append(Line5)
        r = mid + 2
        c = mid + 2 
        x = 4
        dir = 0  
        while x < n-1 :
            line = []
            if dir == 0: #Move left
                r, c = moveleft(r, c, x, Lines, line, arr)
                dir = 1

            elif dir == 1: #move up
                r, c = moveup(r, c, x, Lines, line, arr)
                dir = 2
                x += 1
                print(x)

            elif dir == 2: #move right
                r, c = moveright(r, c, x, Lines, line, arr)
                dir = 3

            elif dir == 3: #move down
                r, c = movedown(r, c, x, Lines, line, arr)
                dir = 0
                x += 1
                print(x)

            else: #If direction is not set
                print("Invalid direction")


        if x == n-1:

            if n%2 != 0:
                li = []
                r, c = moveleft(r, c, x, Lines, li, arr)
                #move up
                li = []
                r, c = moveup(r, c, x, Lines, li, arr)
                #move right
                li = []
                r, c = moveright(r, c, x, Lines, li, arr)
            else:
                #move right
                li = []
                r, c = moveright(r, c, x, Lines, li, arr)
                #move down
                li = []
                r, c = movedown(r, c, x, Lines, li, arr)
                #move left
                li = []
                r, c = moveleft(r, c, x, Lines, li, arr)

    for row in Lines:
        printLines(row)
    print("\n",len(Lines))

    
#Entry point of the Program
if __name__ == "__main__":
    #Input the order of Square Matrix
    n = int(input("Enter the Order of the dots: "))
    findPath(n)
