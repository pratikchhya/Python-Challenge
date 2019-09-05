import os
import csv
pypoll = os.path.join('election_data.csv')
candidates = []
votes = []
names = []
percentage = []
count_candidates = 0
with open (pypoll, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")
   csvheader=next(csvreader)
   for row in csvreader:
       candidates.append(row[2])
   total_votes = len(candidates)
for x in set(candidates):
   candidate_counts = candidates.count(x)
   votes.append(candidate_counts)
   names.append(x)
   total_percent = round((candidate_counts/total_votes) * 100, 1)
   total_percent="%.3f%%" % total_percent
   percentage.append(total_percent)
   count_candidates += 1 #Iterate through each unqiue candidate
winner = names[votes.index(max(votes))]
print("Election Results")
print("-----------------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------------")
for i in range(count_candidates):
   print(f'{names[i]}: {percentage[i]} ({votes[i]})')
print("-----------------------------------")
print(f'Winner: {winner}')
print("-----------------------------------")

output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(count_candidates):
    line = str(f"{names[i]}: {str(percentage[i])} ({str(votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
