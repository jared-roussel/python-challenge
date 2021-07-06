#Import dependencies and libraries
import os
import csv

#Identify location of csv file
csv_file_path = os.path.join("Resources","budget_data.csv.csv")

#Open and read csv file
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

print(csv_reader)


