# Your solution for part c
monthly_salary = float(input("What is your monthly salary? "))
percentage_saved = float(input("Enter the percentage to be save as a decimals: "))
total_cost = float(input("What is the cost of your dream car? "))
percentage_increase = float(input("Enter the increase in said car's price in decimals: "))
salary_raise=.12
interest_rate = 0.01

current_savings = 0
time_estimate = 0

while True:
	for x in range(1,13):
		current_savings *= 1.01
		current_savings += monthly_salary*percentage_saved
		time_estimate += 1
		#print(time_estimate, monthly_salary, current_savings)
		if x%6 == 0:
			#print(x, f'its {time_estimate} now, promo')
			monthly_salary *= 1 + salary_raise
		#print(time_estimate, current_savings)
		if current_savings >= total_cost:
			break
	if current_savings >= total_cost:
		break
	else:
		total_cost += total_cost*percentage_increase	
		#print(f'its {time_estimate} now, increase')

print("Number of months: " + str(time_estimate))