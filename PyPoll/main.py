# import modules
import os
import csv

# set path of csv
csvpath = os.path.join('Resources','election_data.csv')

#dictionary for candidates and vote counts
election_info = {}

# total votes set to 0 for counter
votes = 0

# read csv
with open(csvpath, newline='') as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    #print(election)

    # read out header row
    election_header = next(election)
    # print(election_header)

    # creates election_info dictionary of candidates from Candidate 
    # column of file to only get each name once; count 
    # votes for each candidate
    # https://developers.google.com/edu/python/dict-files
    total_votes = 0
    for row in election: 
        total_votes += 1
        if row[2] in election_info.keys():
            election_info[row[2]] = election_info[row[2]] + 1
        else:
            election_info[row[2]] = 1

# set variables candidates and each vote count as lists
candidates = []
vote_count = []

# using the election_info dictionary keys and values, 
# fill the candidate and vote count lists
# .items() will return the keys and values of the 
# dictionary
#https://www.geeksforgeeks.org/python-dictionary-items-method/
for key, value in election_info.items():
    candidates.append(key)
    vote_count.append(value)
#print(candidates)
#print(vote_count)

# percentage of votes list; using a list because 
# we've established a list of candidates and list of
# their vote counts. We will add their percentage of 
# votes as a list
vote_percentage = []
for votes in vote_count:
    vote_percentage.append(round(votes/total_votes*100, 3))
#print(vote_percentage)

# create a tuple of organized data based on 
# above results
organized_election = list(zip(candidates, vote_count, vote_percentage))
#print(organized_election)

# variable for the winner as a list
winner = []

for name in organized_election:
    if max(vote_count) == name[1]:
        winner.append(name[0])

# string with first entry of winner
celebrator = winner[0]
#print(celebrator)

# results
output_file = output_file = os.path.join('Resources', 'pypoll_results.txt')

with open(output_file, 'w', newline='') as txtfile:
    txtfile.writelines('Election Results\n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for item in organized_election:
        txtfile.writelines(item[0] + ": " + str(item[2]) +'%  (' + str(item[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + celebrator + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())