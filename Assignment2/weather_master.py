"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1

def main():
	"""
	This program can find the highest temperature,Lowest Temperature,Average and cold days
	"""
	print('stanCode "Weather Master 4.0"!')
	new_data = int(input('Next Temperature : (or '+str(EXIT)+' to quit)?'))
	# count cold days
	cold = 0
	# count total days for average
	n = 1
	total = 0
	if new_data == EXIT:
		print('No temperatures were entered.')
	else:
		high = new_data
		low = new_data
		total += new_data
		avg = total/n
		if new_data < 16:
			cold += 1
		while True:
			new_data2 = int(input('Next Temperature : (or '+str(EXIT)+' to quit)?'))
			if new_data2 == EXIT:
				break
			if new_data2 > high:
				high = new_data2
			if new_data2 < low:
				low = new_data2
			n += 1
			total += new_data2
			avg = total/n
			if new_data2 < 16:
				cold += 1


		print('Highest Temperature = ' + str(high))
		print('Lowest Temperature = ' + str(low))
		print('Average = ' + str(avg))
		print(str(cold)+'cold day(s)')






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
