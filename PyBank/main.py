# import modules
import os
import csv

# read csv file
file_path = os.path.join("Resources", "budget_data.csv")
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    # extract header
    header = next(csvreader)

    #initialize lists
    dates = []
    profits = []
    changes = []

    # loop through rows in csv file while populating lists
    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))

        # a neccesary check since change cannot be calculated for first month
        if len(profits) > 1:
            changes.append(profits[-1] - profits[-2])   # change = current - previous profits

# calculate average of changes
avg_change = sum(changes)/len(changes)

# find dates of greatest increase/decrease
index = changes.index(max(changes)) + 1     # +1 offset since changes list is shorter by one
max_change_date = dates[index]

index = changes.index(min(changes)) + 1
min_change_date = dates[index]

# make list to store lines to print out
res_lines = []
res_lines.append("Financial Analysis")
res_lines.append("----------------------------")
res_lines.append(f"Total Months: {len(dates)}")
res_lines.append(f"Net Total: ${sum(profits)}")
res_lines.append(f"Average Change: ${round(avg_change, 2)}")
res_lines.append(f"Greatest Increase in Profits: {max_change_date} (${max(changes)})")
res_lines.append(f"Greatest Decrease in Profits: {min_change_date} (${min(changes)})")

# print out to terminal
print("\n")
for line in res_lines:
    print(line)
print("\n")

# print results to text file
output_path = os.path.join("analysis", "results.txt")
with open(output_path, "w") as output_file:
    for line in res_lines:
        output_file.write(line + "\n")