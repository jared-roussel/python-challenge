#Import dependencies and libraries
import os
import csv

#Identify location of csv file
file_name = os.path.join('PyBank','Resources','budget_data.csv')

#Initialize empty lists for tracking changes
header_names = []
monthly_dates = []
profit_losses = []
m2m_change = []


#Open and read csv file
with open(file_name,"r") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)
    header_names = csv_header
    #print(header_names)


    #Read and append to lists in rows
    for rows in csv_reader:
        monthly_dates.append(rows[0])
        profit_losses.append(rows[1])
        #print(monthly_dates)
        #print(profit_losses)

    #Count the months in the file to get the total # of months
    total_months = 0
    for months in monthly_dates:
        total_months += 1
    #print(total_months) Answer is 86

    #Add profit and losses together for each month
    profits = 0 
    for rows in profit_losses:
        profits += int(rows)
    #print(f"{profits}")

    #Calculate monthly change for each row in the profits / losses column
    

    #Set for loop for capturing the change in profit and loss
    #print(len(profit_losses))
    i = 1
    for i in range(len(profit_losses)-1):
        m2m_change = (int(profit_losses[i+1]) - int(profit_losses[i]))
        print(m2m_change)
    
        #Define function to create average change of profit and losses
    #def average(m2m_change):
        #sum(m2m_change) / len(m2m_change)
    #print(sum(m2m_change))
        
       
    #Print the analysis to the file
    print("----------------------------------------------------------------------------")
    print("Analysis Section")
    print(" ")
    print(" ")
    print(f"Total Months: {total_months}")
    print(f"Total Profit / Losses: $ {profits}")
    print("Average Monthly Change: ")
    print("----------------------------------------------------------------------------")
    

