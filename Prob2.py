##################################################
# Name: Sam Dyke
# Collaborators: Ben from QUAD Center
# Estimate of time spent (hr): 1.5 hrs.
##################################################


def is_magic_square(array:list[list[int]]) -> bool:
	s1=small[0] #first inner list
	s2=small[1] #second inner list
	s3=small[2] #third inner list
	col = len(small) #sets column = 3
	b=s1[0]+s1[1]+s1[2] #base number to check.
	ill = len(s1) #inner list length

	
	def rcheck(): #checks if rows are equal.
		sumr=0 #row sum
		for i in range(len(s1)):#repeats number of items in inner lists.
			pv=s1[i]
			sumr += pv
		if sumr == b: #if row sum = base:
			sumr-=sumr #resets row sum
			for i in range(len(s2)):#repeats number of items in inner lists.
				pv=s2[i]
				sumr += pv
			if sumr == b:#if row sum = base:
				sumr-=sumr #resets row sum
				for i in range(len(s3)):#repeats number of items in inner lists.
					pv=s3[i]
					sumr += pv
			else:
				return False
		else:
			return False
		if sumr == b:#if row sum = base:
# 			print("true")
			ccheck() #runs column check
		else:
			return False

			
	def ccheck():
		sumc=s1[0]+s2[0]+s3[0] #checks first column
		if sumc == b: #if column sum = base:
			sumc-=sumc #resets column sum
			sumc=s1[1]+s2[1]+s3[1] #finds sum of second column
			if sumc == b: #if second column sum = base:
				sumc-=sumc #resets column sum.
				sumc=s1[2]+s2[2]+s3[2] #finds sum of third column
			else:
				return False
		else:
			return False
		if sumc == b: #if third column sum = base:
#			print("true")
			dcheck() #runs diagonal check
		else:
			return False

	
	def dcheck(): #checks diagonals
		sumd=s1[0]+s2[1]+s3[2] #finds first diagonal sum
		if sumd == b: #if first diagonal sum = base:
			sumd-=sumd #resets diagonal sum
			sumd=s1[2]+s2[1]+s3[0] #finds second diagonal sum
		if sumd == b: #if second diagonal sum = base:
			return True
		else:
			return False
	
	if len(s1) == ill: #following functions check the length of inner lists and make sure they are all equal.
		if len(s2)== ill:
			if len(s3)== ill:
				rcheck()
			else:
				return False
		else:
			return False
	else:
		return False
	
	return dcheck() #if everything is correct, returns True, if not, returns False
			
# 	print(type(is_magic_square(small)))
		
		

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

