# import stuff
import os
import csv

# read csv file
file_path = os.path.join("Resources","election_data.csv")

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    candidates = {}

    for row in csvreader:
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

total = sum(candidates.values())
max_percent = 0

output_path = os.path.join("analysis","results.txt")
with open(output_path,"w") as output_file:

    output_file.write("Election Results\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Votes: {total}\n")
    output_file.write("---------------------------\n")

    for candidate in candidates:
        percent = candidates[candidate]/total*100
        if percent > max_percent:
            max_percent = percent
            winner = candidate
        percent = round(percent, 2)
        output_file.write(f"{candidate}: {percent}% ({candidates[candidate]})\n")

    output_file.write("---------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("---------------------------\n")

with open(output_path,'r') as output_file:

    lines = output_file.readlines()

    print("\n")

    for line in lines:
        print(line[:-1])
