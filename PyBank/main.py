#Import dependencies and libraries
import os
import csv

#Identify location of csv file
csv_file_path = os.path.join("..","Resources","budget_data.csv") 

#Open and read csvfile
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#For row in csv_reader:
#print(csv_reader(row))


