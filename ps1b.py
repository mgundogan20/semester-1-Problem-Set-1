# Your solution for part b
monthly_salary = float(input("What is your monthly salary? "))
percentage_saved = float(input("Enter the percentage to be save as a decimals: "))
total_cost = float(input("What is the cost of your dream car? "))
percentage_increase = float(input("Enter the increase in said car's price in decimals: "))


interest_rate = 0.01
current_savings = 0
time_estimate = 0

while True:
	for x in range(12):
		current_savings *= 1+interest_rate
		current_savings += monthly_salary*percentage_saved
		time_estimate += 1
		if current_savings >= total_cost:
			break
	if current_savings >= total_cost:
		break
	else:
		total_cost += total_cost*percentage_increase	

print("Number of months: " + str(time_estimate))
