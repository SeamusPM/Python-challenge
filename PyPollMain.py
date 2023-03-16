import os
import csv

# Path to collect data from the Resources folder
poll_data_csv = os.path.join("PyPoll","Resources", "election_data.csv")

# Define variables to store data
total_votes = 0
candidates = {}
winner = ""

# Open and read csv
with open(poll_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Loop through the rows of data
    for row in csvreader:
        # Count the total number of votes cast
        total_votes += 1
        
        # Get the candidate name from each row
        candidate_name = row[2]

        # Add the candidate to the dictionary if they're not already in it
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        
        # Increment the vote count for the candidate
        candidates[candidate_name] += 1

# Determine the winner
max_votes = 0
for candidate in candidates:
    votes = candidates[candidate]
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    vote_percentage = candidates[candidate] / total_votes * 100
    vote_count = candidates[candidate]
    print(f"{candidate}: {vote_percentage:.3f}% ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_path = os.path.join("PyPoll","Analysis", "election_results.txt")
with open(output_path, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate in candidates:
        vote_percentage = candidates[candidate] / total_votes * 100
        vote_count = candidates[candidate]
        outfile.write(f"{candidate}: {vote_percentage:.3f}% ({vote_count})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")

