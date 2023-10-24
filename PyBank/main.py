# Dependencies
import csv
import os
# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # Read the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# find the dates associated with the greatest values
greatest_increase_index = net_change_list.index(greatest_increase[1])
greatest_increase_date = month_of_change[greatest_increase_index]

greatest_decrease_index = net_change_list.index(greatest_decrease[1])
greatest_decrease_date = month_of_change[greatest_decrease_index]

## print the results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Average Change: ${net_monthly_avg:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Export to txt file
output_file = os.path.join("Analysis", "PyBank_Analysis.txt")
with open(output_file, "w", newline='') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("---------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_net}\n")
    textfile.write(f"Average Change: ${net_monthly_avg:.2f}\n")
    textfile.write(f"Greatest Increase in Profit: {greatest_increase_date} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease[1]})\n")