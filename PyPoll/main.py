# import modules
import os
import csv

# read csv file
file_path = os.path.join("Resources","election_data.csv")

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # extract header
    header = next(csvreader)

    # initialize set to store candidates and their votes
    candidates = {}

    # loop through rows in csv file
    for row in csvreader:
        # if candidate is not already in set, add to set with 1 vote
        if row[2] not in candidates:
            candidates[row[2]] = 1
        
        # else increment vote tally
        else:
            candidates[row[2]] += 1

# sum all votes to get total votes
total = sum(candidates.values())

# initialize variable to store max votes percentage
max_percent = 0

# create list to store lines to print out
res_lines = []
res_lines.append("Election Results")
res_lines.append("---------------------------")
res_lines.append(f"Total Votes: {total}")
res_lines.append("---------------------------")

# loop through generated candidates set
for candidate in candidates:
    # calculate percentage of total votes
    percent = candidates[candidate]/total*100

    # update winner and greatest percentage found
    if percent > max_percent:
        max_percent = percent
        winner = candidate
    
    # round to 2 decimal places for cleanliness
    percent = round(percent, 2)

    # print row for candidate along with votes and % of total
    res_lines.append(f"{candidate}: {percent}% ({candidates[candidate]})")

# print out winner
res_lines.append("---------------------------")
res_lines.append(f"Winner: {winner}")
res_lines.append("---------------------------")

# print out to terminal
print("\n")
for line in res_lines:
    print(line)
print("\n")

# print results to text file
output_path = os.path.join("analysis","results.txt")
with open(output_path,"w") as output_file:
    for line in res_lines:
        output_file.write(line + "\n")