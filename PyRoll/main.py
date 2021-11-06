#Import dependencies and libraries
import os
import csv
from collections import Counter

#Identify location of csv file
#csv_file_path = os.path("Resources","election_data.csv") 
file_name = os.path.join('PyRoll','Resources','election_data.csv')

#Initialize empty lists
#fields = []
#rows = []
voter_ID = []
candidates = []
candidate_vote_list = []
total_votes = 0


#Open and read csvfile
with open(file_name,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    print(csv_reader)

    #Read and append to lists in rows
    for rows in csv_reader:
        total_votes += 1
        voter_ID.append(rows[0])
        candidates.append(rows[2])
print(total_votes)

#Sort candidates to group the same candidate together for counting
candidates_sorted = sorted(candidates)
candidate_votes = Counter(candidates_sorted)
top_candidates = candidate_votes.items()

#Append candidates to the vote list
for candidate in top_candidates:
    candidate_vote_list.append(candidate)
    

#Calculate votes per candidate
khan_votes_perc = format((candidate_vote_list[2][1])*100/total_votes,'.3f')
correy_votes_perc = format((candidate_vote_list[1][1])*100/total_votes,'.3f')
li_votes_perc = format((candidate_vote_list[3][1])*100/total_votes,'.3f')
otooley_votes_perc = format((candidate_vote_list[4][1])*100/total_votes,'.3f')

#Print the analysis to the terminal
print("----------------------------------------------------------------------------")
print("Election Results")
print(" ")
print(f"Total Votes: {total_votes} cast in election")
print("----------------------------------------------------------------------------")
print(f"{candidate_vote_list[2][0]}: {khan_votes_perc} ({candidate_vote_list[2][1]}) ")
print(f"{candidate_vote_list[1][0]}: {correy_votes_perc} ({candidate_vote_list[1][1]}) ")
print(f"{candidate_vote_list[3][0]}: {li_votes_perc} ({candidate_vote_list[3][1]}) ")
print(f"{candidate_vote_list[4][0]}: {otooley_votes_perc} ({candidate_vote_list[4][1]}) ")
print("----------------------------------------------------------------------------")
print(f"Winner: {candidate_vote_list[2][0]}")

#Create lines for creation of txt file
lines = ["Election Results",
" ",
f"Total Votes: {total_votes} cast in election",
f"{candidate_vote_list[2][0]}: {khan_votes_perc} ({candidate_vote_list[2][1]})",
f"{candidate_vote_list[1][0]}: {correy_votes_perc} ({candidate_vote_list[1][1]})",
f"{candidate_vote_list[3][0]}: {li_votes_perc} ({candidate_vote_list[3][1]})",
f"{candidate_vote_list[4][0]}: {otooley_votes_perc} ({candidate_vote_list[4][1]})",
f"Winner: {candidate_vote_list[2][0]}"]


#r allows for a raw string value to add to the file_path
save_path = (r'C:\Users\12254\personal-class\python-challenge\python-challenge\PyRoll\Analysis')
new_file_name = 'election_results.txt'
file_path = os.path.join(save_path, new_file_name)
print(file_path)
new_file = open(file_path,"a")

#write to new file
new_file.writelines('\n'.join(lines))