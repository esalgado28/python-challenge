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

# print results to text file
output_path = os.path.join("analysis","results.txt")
with open(output_path,"w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Votes: {total}\n")
    output_file.write("---------------------------\n")

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
        output_file.write(f"{candidate}: {percent}% ({candidates[candidate]})\n")

    # print out winner
    output_file.write("---------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("---------------------------\n")

# read text file and print to terminal
with open(output_path,'r') as output_file:

    lines = output_file.readlines()

    print("\n")

    for line in lines:
        print(line[:-1])
