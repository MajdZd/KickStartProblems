def main(t): # the main function that excecutes all the functions
	res  = []
	for test in range(0, t): # solve for each test case
		tornPages = []
		readers = []
		p = []
		firstLine = input().split(' ')
		firstLine
		n = int(firstLine[0]) # number of pages in a book
		m = int(firstLine[1]) # number of torn pages
		q = int(firstLine[2]) # number of readers
		x = input().split(' ')
		y = input().split(' ')
		for i in x:
			tornPages.append(int(i)) 
		for j in y:
			readers.append(int(j))
		#print(tornPages)
		#print(readers)
		
		p = pages(n,tornPages) # the pages that aren't torn apart

		c = 0
		for r in readers:
			a = multi(r, p) # check how many page numbers are multiples of the reader number
			c += a
		res.append(c)

	
	return res

def pages(p, tornPages):
	r = []
	tornPages.sort()
	c = 0
	for i in range(1, p+1): # for each i from 1 to p (the number of pages)
		if c<len(tornPages): # if all torn pages are checked
			if i != tornPages[c]: # check if i is not a torn page
				r.append(i) # add i to the available pages
			elif i == tornPages[c]: # if i is torn
				c += 1 # go to the next torn page
		else:
			r.append(i) # if all the torn pages were removed add every i until we reach p after that
	return r

def multi(reader, pages):
	c = 0
	for i in pages: # for each page
		if (i % reader) == 0: # check if it's a mod to the reader number
			c += 1 # the number of pages the reader will read
	return c


t = input()
t = int(t)
count = 1
for answer in main(t):
	print("Case #" + str(count) + ": " + str(answer))
	count += 1
