import csv
import os

in_file = os.path.join("PyBank","Resources", "budget_data.csv")

file_output = "../Analysis/budget_data.txt"

total_month = 0
total_profit = 0
total_change = 0
change_month = 0


with open(in_file) as bank_file:
    content = csv.reader(bank_file)

    Header = next(content)
    Jan_row = next(content)
    
    total_month += 1
    total_profit += int(Jan_row[1])

    previous_profit = int(Jan_row[1])

    for row in content:
        total_month += 1
        total_profit += int(row[1])

        change = int(row[1]) - previous_profit

        total_change += change 
        change_month += 1
    
        previous_profit = int(row[1])

print(total_month, total_profit)  


        
       

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: ${total_change/change_month:,.2f}
Greatest Increase in Profits: max({"Date": {change}})
Greatest Decrease in Profits: min({"Date": {change}})
"""


print(output)
with open(file_output, "w") as pybank:
    pybank.write(output)
