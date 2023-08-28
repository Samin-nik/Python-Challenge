#access and import CSV

import os
import csv

# Specify the correct file path based on the given directory structure
# desktop_path = os.path.expanduser("~/Desktop")
# module_path = os.path.join(desktop_path, "module-03-starter-code")
# pypoll_path = os.path.join(module_path, "pypoll")
pypoll_csv = os.path.join( "Resources", "election_data.csv")

# Open and read the CSV file

with open(pypoll_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    total_votes= 0
    candidate_votes={} #why is this a list and next one a dictionary?
    candidate_names= []
    
    next(csv_reader) #skip header
    for row in csv_reader:
        
        total_votes +=1
        candidate_name = row[2]  
        if candidate_name not in candidate_names:
            candidate_names.append(candidate_name)
            candidate_votes[candidate_name]=1 
        else:
            
            candidate_votes[candidate_name] +=1 
print ("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")   
  
for candidate_name in candidate_names:
    votes= candidate_votes[candidate_name] 
    vote_percentage= (votes/total_votes)*100
    formatted_percentage = "{:.3f}".format(vote_percentage)  # Format to three decimal places
    print(f"{candidate_name}: {formatted_percentage}% ({votes})")

winner = max(candidate_votes, key=candidate_votes.get)





print("-----------------------------")
print(F"Winner: {winner}")
print("-----------------------------")

output_file = os.path.join("results.txt")
with open(output_file, 'w') as text_file:
    
    text_file.write("Election Results\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-----------------------------\n")
    for candidate_name in candidate_names:
        votes= candidate_votes[candidate_name] 
        vote_percentage= (votes/total_votes)*100
        formatted_percentage = "{:.3f}".format(vote_percentage)  # Format to three decimal places
        text_file.write(f"{candidate_name}: {formatted_percentage}% ({votes})\n")
    text_file.write("-----------------------------\n")
    text_file.write(F"Winner: {winner}\n")
    text_file.write("-----------------------------\n")