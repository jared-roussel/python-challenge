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
candidate_votes = []
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

candidates_sorted = sorted(candidates)
#print(candidates_sorted)
#candidates_list = candidates
candidate_votes = Counter(candidates_sorted)

print(candidate_votes)
print(candidate_votes)

#def candidate_count(candidates_sorted):
    #candidate_vote_count = 0 
    #for candidate in candidates:
        #if (candidate == candidate_list):
            #candidate_vote_count += 1
    #return candidate_vote_count
#print(candidate_vote_count)



