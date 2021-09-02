#Import dependencies and libraries
import os
import csv

#Identify location of csv file
#csv_file_path = os.path("Resources","election_data.csv") 
file_name = os.path.join('PyRoll','Resources','election_data.csv')

#Initialize empty lists
#fields = []
#rows = []
voter_ID = []
candidates = []


#Open and read csvfile
with open(file_name,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    print(csv_reader)

    #Read and append to lists in rows
    for rows in csv_reader:
        voter_ID.append(rows[0])
        candidates.append(rows[2])

def candidate_count(candidates, index(candidates)):
    candidate_vote_count = 0 
    for candidate in candidates[0:10]:
        if (candidate == candidate):
            candidate_vote_count += 1
print(candidate_vote_count)

#print(voter_ID)
#print(candidates)

vote_count = len(voter_ID)
print(vote_count)

