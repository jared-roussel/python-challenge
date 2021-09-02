#Import dependencies and libraries
import os
import csv

#Identify location of csv file
file_name = os.path.join('PyBank','Resources','budget_data.csv')

#Initialize empty lists for tracking changes
header_names = []
monthly_dates = []
profit_losses = []
m2m_change_list= []


#Open and read csv file
with open(file_name,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)
    header_names = csv_header


    #Read and append to lists in rows
    for rows in csv_reader:
        monthly_dates.append(rows[0])
        profit_losses.append(rows[1])


    #Count the months in the file to get the total # of months
    total_months = 0
    for months in monthly_dates:
        total_months += 1

    #Add profit and losses together for each month
    profits = 0 
    for rows in profit_losses:
        profits += int(rows)


    #Set for loop for capturing the change in profit and loss
    i = 1
    change_avg = 0
    for i in range(len(profit_losses)-1):
        m2m_change = (int(profit_losses[i+1]) - int(profit_losses[i]))
        m2m_change_list.append(m2m_change)


#print(len(m2m_change_list))
#print(len(monthly_dates))

max_m2m = max(m2m_change_list)
min_m2m = min(m2m_change_list)
avg_m2m = sum(m2m_change_list) / len(m2m_change_list)
rounded_avg = round(avg_m2m,2)
#print(avg_m2m)

max_m2m_index = m2m_change_list.index(max_m2m)
min_m2m_index = m2m_change_list.index(min_m2m)

#print(max_m2m_index)
#print(min_m2m_index)

#Print the analysis to the file
print("----------------------------------------------------------------------------")
print("Analysis Section")
print(" ")
print(f"Total Months: {total_months}")
print(f"Total Profit / Losses: $ {profits}")
print(f"Average Monthly Change: $ {rounded_avg}")
print(f"Greatest Increase in Profits: {monthly_dates[max_m2m_index+1]} ($ {max_m2m})")
print(f"Greatest Decrease in Profits: {monthly_dates[min_m2m_index+1]} ($ {min_m2m})")
print("----------------------------------------------------------------------------")

lines = ["Analysis Section",
" ",
f"Total Months: {total_months}",
f"Total Profit / Losses: $ {profits}",
f"Average Monthly Change: $ {rounded_avg}",
f"Greatest Increase in Profits: {monthly_dates[max_m2m_index+1]} ($ {max_m2m})",
f"Greatest Decrease in Profits: {monthly_dates[min_m2m_index+1]} ($ {min_m2m})"]
#print(lines)

#r allows for a raw string value to add to the file_path
save_path = (r'C:\Users\12254\personal-class\python-challenge\python-challenge\PyBank\Analysis')
new_file_name = 'analysis.txt'
file_path = os.path.join(save_path, new_file_name)
print(file_path)
new_file = open(file_path,"a")
#with open("analysis.txt","a") as new_file:
new_file.writelines('\n'.join(lines))