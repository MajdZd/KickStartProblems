def hmax(pa):
    # finds out the max value such for
    # the number of refrences of the research
    # papers and the number of times they occur
    pa.sort()
    for a in range(0, len(pa)):
        c = 0
        for b in range(a, len(pa)):
            if pa[b] >= pa[a]:
                c += 1
        if c <= pa[a]:
            return c

def fullInput(a):
    # returns the hmax of every iteration
    # of the test cases
    res = []
    for i in range(0, len(a)):
        arr = []
        for k in range(0, i+1):
            arr.append(a[k])
        res.append(hmax(arr))
    return res
       
# test cases
t = input()
t = int(t)

# turn the array into a string format for output
def toString(arr):
    string = ''
    for r in arr:
        string += str(r) + " "
    return string

inputs = []

# run the process on every test case
for i in range(0, t):
    n = input()
    a = input()
    n = int(n)
    a = a.split()
    for x in range(0, len(a)):
        a[x] = int(a[x])
    inputs.append(a)
    
for j in inputs:
    res = toString(fullInput(j))
    print("Case #" + str(inputs.index(j)+1) + ": " + res)
        
