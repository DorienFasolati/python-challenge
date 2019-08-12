import os
import csv

input_file = os.path.expanduser(r'~\Desktop\RU Bootcamp\Git Repo\RUTJC201907DATA3\02-Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv')
output_file = os.path.expanduser(r'~\Desktop\RU Bootcamp\Git Repo\RUTJC201907DATA3\02-Homework\03-Python\Instructions\PyBank\Resources\budget_analysis.csv')

with open(input_file, newline = "") as csv_file:
    budget_data = csv.reader(csv_file, delimiter = ",")
    header = next(budget_data)

    revenue = []
    date = []
    change_diff = []

    for row in budget_data:
        revenue.append(float(row[1]))
        date.append(row[0])

    for i in range(1,len(revenue)):
        change_diff.append(revenue[i] - revenue[i-1])   
        avg_change = sum(change_diff)/len(change_diff)
        max_change = max(change_diff)
        min_change = min(change_diff)
        max_change_date = str(date[change_diff.index(max(change_diff))+1])
        min_change_date = str(date[change_diff.index(min(change_diff))+1])
        total_months = str(len(date))
        avg_change_str = str(round(avg_change))

with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    print(f"Financial Analysis")
    file.write("**********************\n")
    print(f"**********************")
    file.write("Total Months:" +str(total_months)+"\n")
    print("Total Months:", total_months)
    file.write("Total Revenue: " +str(round(sum(revenue)))+"\n")
    print("Total Revenue:", sum(revenue))
    file.write("Average Revenue Change: " +avg_change_str+"\n")
    print("Average Revenue Change: $", round(avg_change))
    file.write("Greatest Increase in Revenue: " +str(max_change_date)+ " ($"+str(round(max_change)) +")\n")
    print("Greatest Increase in Revenue: " +max_change_date+ " ($"+str(round(max_change))+")")
    file.write("Greatest Decrease in Revenue: "+str(min_change_date)+" ($"+str(round(min_change))+")\n")
    print("Greatest Increase in Revenue: "+min_change_date+" ($"+str(round(min_change))+")")
    