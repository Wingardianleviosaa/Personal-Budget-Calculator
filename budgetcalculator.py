try:
    income= int(input("Enter your income per month:"))
    rent=int(input("Rent: "))
    food=int(input("Food: "))
    travel=int(input("Travel: "))
    misc=int(input("Miscellaneous: "))
except:
    print ("incorrect data! RETRY ")
#To calculate and classify
totalexp= rent+food+travel+misc
amt_left= income-totalexp
print("Your total expenditure is",totalexp,", hence the amount left is ",amt_left)
if amt_left <=0:
    advice = "Spend carefully! Remaining funds are low."
    print(advice)
elif amt_left <=1000:
    advice="Tight budget! Spend wisely on non-essentials!"
    print(advice)
else:
    advice="Adequate savings! Consider emergency fund."
    print(advice)
#To generate and save report
summary= {"Income":income, "Expenses":totalexp,"Remaining":amt_left, "Advice given ":advice }
value = str(summary)
with open('budget.txt', 'w') as f:
    f.write(value)