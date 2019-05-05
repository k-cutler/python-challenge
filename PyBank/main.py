# import modules
import os
import csv

# set path of csv
csvpath = os.path.join('Resources','budget_data.csv')

# create variables 'months' and 'revenue' as lists
months = []
revenue = []

# read csv
with open(csvpath, newline='') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    # print(budget)

    # read out the header row
    budget_header = next(budget)
    # print(f"CSV Header: {budget_header}")
    
    #read each row to ensure it is reading the file
    #for row in budget:
        #print(row)

    # 6. parse into lists
    for row in budget:
        months.append(row[0])
        revenue.append(int(row[1]))
        
# find the total number of months
total_months = len(months)
#print(total_months)

# find total revenue by iterating through revenue column
# adding row 1 to row 2, that total to row 3, etc.
total_revenue = 0
for x in revenue:
    total_revenue += int(x)
#print(total_revenue)

# find average revenue change
    total_revenue_change = 0
    for y in range(total_months):
        total_revenue_change += int(revenue[y]) - int(revenue[y-1])

        # the first_iteration variable is created to remove the first iteration revenue change
        # which, takes the first list element and subtracts it by the last list element.
        first_iteration = (int(revenue[0]) - int(revenue[-1]))
        total_revenue_change_updated = total_revenue_change - first_iteration
        avg_revenue_change = round(total_revenue_change_updated/total_months, 2)
#print(avg_revenue_change) 

# create greatest increase and decrease variables
# for revenue
greatest_increase_revenue = revenue[0]
greatest_decrease_revenue = revenue[0]


for z in range(len(revenue)):
    if revenue[z] >= greatest_increase_revenue:
        greatest_increase_revenue = revenue[z]
        greatest_increase_month = months[z]
    elif revenue[z] <= greatest_decrease_revenue:
        greatest_decrease_revenue = revenue[z]
        greatest_decrease_month = months[z]
#print(greatest_decrease_month)
#print(greatest_decrease_revenue)
#print(greatest_increase_month)
#print(greatest_increase_revenue)

print(f"Financial Analysis\n")
print("--------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Average Change: ${avg_revenue_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_revenue})\n")
print(f"Greatest Increase in Profits: {greatest_decrease_month} (${greatest_decrease_revenue})\n")

# set variable for output file
output_file = os.path.join('Resources', 'pybank_complete.txt')

with open(output_file, 'w', newline='') as writefile:
    writefile.writelines("Financial Analysis")
    writefile.writelines("Total Months: " + str(total_months))
    writefile.writelines("Average Change: $" + str(avg_revenue_change))
    writefile.writelines("Greatest Increase in Profits: " + greatest_increase_month + " ($" + (str(greatest_increase_revenue)) + ")")
    writefile.writelines("Greatest Increase in Profits: " + greatest_decrease_month + " ($" + (str(greatest_decrease_revenue)) + ")")