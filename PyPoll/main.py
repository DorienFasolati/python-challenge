import os
import csv
row_count = 0 
candidate = []
cand_result = {}
winner = ""
votes = 0

input_file = os.path.expanduser(r'~\Desktop\RU Bootcamp\RUTJC201907DATA3\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv')
output_file = os.path.expanduser(r'~\Desktop\RU Bootcamp\RUTJC201907DATA3\02-Homework\03-Python\Instructions\PyPoll\Resources\election_analysis.csv')

with open(input_file, newline = "") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        row_count = row_count + 1
        if row[2] not in candidate:
            candidate = candidate + [row[2]]    

for i in range(len(candidate)):   
    cand_result[candidate[i]] = [0]

with open(input_file,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        if row[2] in cand_result:
            cand_result[row[2]] += [1]

with open(output_file, 'w') as file:
    file.write("***************************\n")
    print("***************************")
    file.write("     Election Result       \n")
    print("        Election Results           ")
    file.write("***************************\n")
    print("***************************")
    file.write("     Total Votes: %d\n" % row_count)
    print(f"  Total Votes: {row_count}")
    file.write("***************************\n")
    print("***************************")
    for i in range(len(candidate)):
        file.write("%s: %d%s (%d)\n" % (candidate[i], round(sum(cand_result[candidate[i]])/row_count*100,2), "%", sum(cand_result[candidate[i]])))
        print(f"{candidate[i]}: {round(sum(cand_result[candidate[i]])/row_count*100,2)}% ({sum(cand_result[candidate[i]])})")
        if sum(cand_result[candidate[i]]) > votes:
            winner = candidate[i]
            votes = sum(cand_result[candidate[i]])
    file.write("***************************\n")
    print("***************************")
    file.write("      Winner is %s\n" % winner)
    print(f"       Winner is {winner}!!!!!!!!!!!!")
    file.write("***************************\n")
    print("***************************")