# Your solution for part d
# Your solution for part d
import math
monthly_salary = float(input("What is your monthly salary? "))
total_cost = float(input("What is the cost of your dream car? "))
percentage_increase = float(input("Enter the increase in said car's price in decimals: "))
salary_raise= float(input("Enter the percentage salary raise, as a decimal: "))
interest_rate = 0.01


def estimate(percentage_saved,): 
	"""
	calculates the difference of savings and total cost at the end of 24 months for a given saving rate
	"""
	global monthly_salary, salary_raise
	global total_cost, percentage_increase
	
	cost = total_cost
	salary = monthly_salary
	percentage_saved /= 10000

	current_savings = 0
	time_estimate = 0

	while True:
		for x in range(1,13):
			current_savings *= 1.01
			current_savings += salary*percentage_saved
			time_estimate += 1
			#print(time_estimate, salary, current_savings)
			if x%6 == 0:
				salary *= 1 + salary_raise
			if time_estimate == 24:
				break
		if time_estimate == 24:
			break
		else:
			cost += cost*percentage_increase
	return(current_savings-cost)


def binarySearch():
	high = 10000
	low = 0
	mid = (high + low)/2
	steps=0
	
	if estimate(high) < 0:
		print("It is not possible to buy the car in two years")
	else:
		while abs(estimate(mid)) > 1000:
			if estimate(mid) >= 0:
				steps += 1
				high = mid
			else:
				steps += 1
				low = mid
			mid = math.ceil((high + low)/2)
		print("Best savings rate: {:.3f}".format(mid/10000))
		print("Steps in bisection search: {:d}".format(steps))

binarySearch()