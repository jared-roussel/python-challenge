#Import dependencies and libraries
import os
import csv

#Identify location of csv file
file_name = os.path.join('PyBank','Resources','budget_data.csv')

#Initialize empty lists for tracking changes
header_names = []
monthly_dates = []
profit_losses = []


#Open and read csv file
with open(file_name,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)
    header_names = csv_header
    print(header_names)
    
    #for rows in csv_reader:
        #print(rows)

    for rows in csv_reader:
        monthly_dates.append(rows[0])
        profit_losses.append(rows[1])
        # print(monthly_dates)
        #print(profit_losses)

