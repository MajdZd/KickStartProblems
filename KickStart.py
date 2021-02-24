def kickCheck(s):
    x = 0
    kick = []
    for i in range(0,len(s)-3):
        if (s[i]+s[i+1]+s[i+2]+s[i+3]) == "KICK":
            kick.append(i+4)
            x += 1
    return kick

def startCheck(s, kick):
    c = 0
    for k in kick:
        for x in range(k, len(s)-4):
            if (s[x]+s[x+1]+s[x+2]+s[x+3]+s[x+4]) == "START":
                c += 1
    return c

def run(t):
    res = []
    b = 0
    for a in range(0, t):
        s = input()
        s = list(s)
        res.append(startCheck(s,kickCheck(s)))
    for b in range(0, t):
        print("Case #" + str(b+1) + ": " + str(res[b]))
       
t = input()
t = int(t)
run(t)
