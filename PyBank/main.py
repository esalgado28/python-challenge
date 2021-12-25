# import stuff
import os
import csv

# read csv file
file_path = os.path.join("Resources","budget_data.csv")
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # extract header
    header = next(csvreader)

    #initialize lists
    dates = []
    profits = []
    changes = []

    # loop through data
    for row in csvreader:
        dates.append(row[0])
        profits.append(int(row[1]))

        if len(profits) > 1:
            changes.append(profits[-1] - profits[-2])

# calculate average of changes
avg_change = sum(changes)/len(changes)
# find date of greatest increase/decrease
index = changes.index(max(changes)) + 1
max_change_date = dates[index]
index = changes.index(min(changes)) + 1
min_change_date = dates[index]

# print results to text file
output_path = os.path.join("analysis","results.txt")
with open(output_path,"w") as output_file:
    output_file.write("Financial Analysis\n") 
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {len(dates)}\n")
    output_file.write(f"Total: ${sum(profits)}\n")
    output_file.write(f"Average Change: ${round(avg_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {max_change_date} (${max(changes)})\n")
    output_file.write(f"Greatest Decrease in Profits: {min_change_date} (${min(changes)})\n")

# read from file and print to terminal
with open(output_path,"r") as output_file:
    lines = output_file.readlines()
    print("\n")

    for line in lines:
        print(line[:-1])

    print("\n")