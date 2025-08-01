monthly_income = int(input("enter your monthly income: "))
monthly_expenses = int(input("enter you total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)