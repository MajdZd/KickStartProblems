# calculates the factorial of any int
def fact(l):
  if l == 1:
    return 1
  return fact(l-1)*l

# takes the array in the given input format and outputs
# and array that represents an int
def digits(a):
	res = []
	for i in range(0, len(a)):
		for j in range(0, a[i]):
			#print(i)
			res.append(i+1)
	print(res)
	return res

# returns the amount of unrepeated ints in the array
def rep(a):
  rs = 0
  a.sort()
  for i in range(0, len(a)):
    if i != len(a)-1:  
      if a[i] != a[i+1]:
        rs += 1
  return rs+1

# replaces index x with index y
def swap(a,x,y):
  if x != y and a[x] != a[y]:
    p = a[x]
    a[x] = a[y]
    a[y] = p
    return a
  else:
    a = []
    return

# outputs all permutations of the given array 
def move(a, c, rec):
  #print("*")
  count.append(1)
  print(count)
  if c == len(a)-1:
    r(a)
    print(a)
    return a
  for i in range(c, len(a)):
    if a[i] != a[c] or len(count)<=rec+len(a): # makes sure that there is no unnecessary repetition
      swap(a,c,i)
      # the recursive call
      move(a,c+1,rec)
      swap(a,c,i)

# stores the permutations in the variable result
def r(a):
  result.extend(a)

# goes through result and checks in the numbers can be divisable by eleven
def check(pa, a):
	for i in range(0, len(pa), len(a)):
		s = 0
		for j in range(i, i+len(a)):
			# if the index is even (starting from 0) add it, if it's odd reduce it from the sum
      if j%2 == 0:
				s += pa[j]
			else:
				s -= pa[j]
		#print(s)
		if s%11 == 0:
			return "YES"
	return "NO"

t = input()
t = int(t)
res = []
k = 1
# excecute for every test case
for x in range(0, t):
	result = []
	count = [] # this is the variable that regulates the amount of recursive function calls
	a = input()
	a = a.split()
	for s in range(0, len(a)):
		a[s] = int(a[s])

	d = digits(a) # take the array and turn it into a number
	rc = rep(d) # the amount of nonrepeating ints
	c = move(d,0,rc) # generate a list of permutations without too much repetion
	#print(result) 
	res.append(check(result, d)) # store the results in res

for r in res:
	print("Case #" + str(k) + ": " + str(r))
	k += 1




