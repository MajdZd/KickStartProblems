# generates a canvas where black is 1 and white is 0
def canva(canvas):
    res = []
    for c in canvas:
        if c == '.':
            res.append(0)
        if c == '#':
            res.append(1)
    return res
# generates all prossible diagnols based on the canvas size     
def slash(n):
    res = []
    for i in range(0, n): # from top right
        ph = []
        for j in range(0, i+1):
            p = i + j*n - j
            ph.append(p)
        res.append(ph)
    for i1 in range(0, n): # from top left
        ph = []
        for j1 in range(0, i1+1):
            p = n + j1 - i1 + j1*n - 1
            ph.append(p)
        res.append(ph)
    for i2 in range(0, n): # from bottom right
        ph = []
        for j2 in range(0, i2+1):
            p = n*(n-1) - j2 + i2 - j2*n
            ph.append(p)
        res.append(ph)
    for i3 in range(0, n): # from bottom left
        ph = []
        for j3 in range(0, i3+1):
            p = n*n - i3 +j3 - j3*n - 1
            ph.append(p)
        res.append(ph)
    return res
            
# solves the problem by comparing diagnol sets in each iteration until canvas is all black
def solve(canvas, n, slash): 
    res = 0
    while 1:
        count = 0
        scorelist = [] # which diagnols set has biggest score
        
        
        for c in canvas:
            if c == 0:
                break
            count += 1
        #print(count)
        if count == n*n:
            break
        
        for e in slash:
            score = 0
            for i in e: # generating scores based on diagnols that generate the most black cells and the least white cells
                if canvas[i] == 0: 
                    score += 1
                elif canvas[i] == 1:
                    score -= 1
            scorelist.append(score)
        cscore = scorelist.index(max(scorelist)) # which diagnol set has the highest score
        #print(slash[cscore])
        
        for x in slash[cscore]: # reversing the color of every cell that has a diagnol applied to it
            if canvas[x] == 0:
                canvas[x] = 1
            elif canvas[x] == 1:
                canvas[x] = 0
        #print(canvas)
        res += 1
    return res
        
        
t = input()
t = int(t)
c = 1
res = []
for tc in range(0, t):  # runs the solution for each test case  
    canvas = []
    line = []
    n = input()
    n = int(n)
    
    for i in range(0, n): 
        line = list(input()) # the input in string form
        canvas.extend(line) # the generated canvas
    res.append(str(solve(canva(canvas), n, slash(n)))) # finding the least number of opperations necessary for every canvas
    
for e in res:
    print("Case #" + str(c) + ": " + e) # outputing results
    c+=1
    
    


    
