from pgl import *
color="red" #color of rectangles.

#1a
def create_histogram_array(data:list[int]):
	array = [] #creates a blank array.
	for i in range(max(data) + 1): #repeats the same number of times as... 
	#...the highest value in the list.
		pher=0		#placeholder set to 0 at the start of each run.
		for n in (PI_DIGITS): #checks all numbers in the first 20 digits of pi.
			if i == n in PI_DIGITS: #checks if a particular digit matches i.
				pher+=1 #will update pher every time the previous condition is met.
			an=str(pher) #sets variable an to pher and makes it a string.
		array.append(pher) #appends original array with the number of times a value appears in pi digits.
	return(array) #returns array.
		
			

#1b

def print_histogram(hist:list[int]):
	for i in range(len(hist)): #will repeat the following code however many items are in hist.
		n=hist[i] #sets n equal to the value of the current item in hist.
		print(str(i) + ": " + "*" * n) #prints number of times a value appears in PI DIGITS.

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
	gw = GWindow(width, height)
	def my_rect(x,y,w,h,color): #creates rectangles for histogram.
		rect = GRect(x,y,w,h)
		rect.set_filled(True)
		rect.set_color(color)
		gw.add(rect)
	for i in range(len(hist)): #will repeat the following code however many items are in hist.
		sl=40 #side length
		n=hist[i] #sets n equal to the value of the current item in hist.
		x=sl+sl*i #sets x coord of rectangle
		y=height #sets the starting height of the bricks as maximum height.
		w=-sl #sets width of rectangle
		h=-sl*n #sets the height of the rectangle based on number of times a value appears in PI DIGITS.
		my_rect(x,y,w,h,color)
# 
#     pass

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test


