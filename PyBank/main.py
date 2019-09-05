# First import the os module
import os
# Module for reading CSV files
import csv
budget_data = os.path.join("budget_data.csv")
months = []
revenue = []
profits = []
# Open the CSV File
with open(budget_data, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")
   csv_header = next(csvreader)
   for row in csvreader:
       months.append(row[0])
       revenue.append(int(row[1]))
   # calculate total length of months
   total_months = len(months)
   # calculate the net total
   total_revenue = sum(revenue)
   for i in range(1, len(revenue)):
       revenue_change = ((int(revenue[i]) - int(revenue[i-1])))
       profits.append(revenue_change)
   #The average of the changes in "Profit/Losses"
   avg_change = sum(profits) / len(profits)
   #The greatest increase in profits (date and amount)
   Greatest_increase = max(profits)
   Greatest_date = (months[profits.index(Greatest_increase)+1])
   #The greatest decrease in losses (date and amount)
   Greatest_decrease = min(profits)
   loss_date = (months[profits.index(Greatest_decrease)+1])
print("Financial Analysis")
print("----------------------")
print(f"Total months: {str(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})")
print(f"Greatest Decrease in Profits: {loss_date} (${str(Greatest_decrease)})")

output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = "--------------------------"
line3 = (f"Total months: {str(total_months)}")
line4 = (f"Total: ${str(total_revenue)}")
line5 = (f"Average Change: ${str(round(avg_change,2))}")
line6 = (f"Greatest Increase in Profits: {Greatest_date} (${str(Greatest_increase)})")
line7 = (f"Greatest Decrease in Profits: {loss_date} (${str(Greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))

