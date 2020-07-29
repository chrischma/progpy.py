import os

# Getting the size of the window to perfectly scale the bar.
window_size = os.get_terminal_size().columns 

# Calculating some default sizes. We also reserve 5 characters for additional info to be printed. 
short 	= window_size*0.25-5					
medium 	= window_size*0.5-5					
maximum = window_size-5

# Chose a length here. Options are short, medium and maximum, as defined above. Or any number you wish.
length = medium 

# If set to True, the bar will be printed automatically. If false, progress_bar just returns the final string.		
auto_print = True 				

def progress_bar(split,total):

	# Creating an empty list an string we'll fill later.
	progressbar_list = []
	pb_string = ""
	percent = (split/total)

	# Calcualting, how long the black bar will be.
	length_of_black_bar = percent*length

	# Drawing the black bar.
	while length_of_black_bar > 0:
		progressbar_list.append("█")
		length_of_black_bar -= 1

	# Drawing the whitespace next to the black bar.
	while len(progressbar_list) < length:
		progressbar_list.append("-")

	# Creating a the final string.
	bar_string = f'{pb_string.join(progressbar_list)} {round(percent*100)}% '

	# Print the bar if wished.
	if auto_print == True:
		print(bar_string)

	else:
		return bar_string


# Examples
progress_bar(50,500)





