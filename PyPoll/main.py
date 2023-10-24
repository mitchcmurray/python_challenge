import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#set variables
totalvotes = 0
candidates = {}
winner = ""
winner_votes = 0

#Read csv file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader) # skip header

    for row in csvreader:
        totalvotes += 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
percentage = {}
max_votes = 0

for candidate, votes in candidates.items():
    percentage[candidate] = (votes / totalvotes) * 100
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

for candidate, votes in candidates.items():
    print(f"{candidate}: {percentage[candidate]:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export to a text file
output_file = os.path.join("Analysis", "PyPoll_Analysis")
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write("-------------------------\n")

    for candidate, votes in candidates.items():
        file.write(f"{candidate}: {percentage[candidate]:.3f}% ({votes})\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
