# Your solution for part a
monthly_salary = float(input("Enter your monthly salary: "))
percentage_saved = float(input("Enter the percentage to save, as a decimal: "))
total_cost = float(input("Enter the cost of the dream car: "))

interest_rate = 0.01
current_savings = 0
time_estimate = 0

while current_savings < total_cost:
	current_savings *= 1+interest_rate
	current_savings += monthly_salary*percentage_saved
	time_estimate += 1

print("Number of months: " + str(time_estimate))