#Import dependencies and libraries
import os
import csv

#Identify location of csv file
#csv_file_path = os.path("Resources","election_data.csv") 
file_name = os.path.join("Resources","election_data.csv")
fields = []
rows = []

#Open and read csvfile
with open(file_name,"r") as csv_file:
    csv_reader = csv.read(csv_file,delimiter=",")