import csv


file_input = os.path.join("PyPoll", Resources", "election_data.csv") 

file_output = "../Analysis/election_data.txt"

total_vote = 0
candidate_list = []  # From YouTube.com, Unit 3 - PyPoll Homework Walkthrough
per_candidate_count = {}

winner = "" # From YouTube.com, Unit 3 - PyPoll Homework Walkthrough
winner_count =  # From YouTube.com, Unit 3 - PyPoll Homework Walkthrough


with open(file_input) as election_file:
    reader = csv.Dictreader(election_file)

Header = next(content)

for row in reader:
    total_vote += 1
    candidate_name = row["Candidate"]
    
    if candidate_name not in candidate_list:
        candidate_list.append(candidate_name)
        
        per_candidate_count[candidate_name] = 0
    
        per_candidate_count[candidate_name] +=1

    for candidate in per_candidate_count: # From YouTube.com, Unit 3 - PyPoll Homework Walkthrough
        candidate_total = per_candidate_count.get(candidate)
        candidate_percentage = float(per_candidate_count) /float(total_vote) * 100

        if (candidate_total > winner_count): # From YouTube.com, Unit 3 - PyPoll Homework Walkthrough
                winner_count = candidate_total
                winner_candidate = candidate


        election_results = f"{candidate}: {candidate_percentage: .3f}% ({candidate_total}" 
        print(election_results)




        
output = f"""
Election Results
----------------------------
Total Votes: {total_vote}
____________________________

Charles Casper Stockham: f"{Charles Casper Stockham}: {candidate_percentage: .3f}% ({candidate_total}" 
Diana DeGette: f"{Diana DeGette}: {candidate_percentage: .3f}% ({candidate_total}" 
Raymon Anthony Doane: f"{Raymon Anthony Doane}: {candidate_percentage: .3f}% ({candidate_total}" 
____________________________

Winner: Diana DeGette
"""

print(output)

with open(file_output, "w") as pybank:
    pybank.write(output)