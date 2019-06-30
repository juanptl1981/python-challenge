#import modules
import os
import csv

#create part variable
csvpath = os.path.join('election_data.csv')
count_months = 0
#using the with and open methods we initiate the file handling. 

with open(csvpath, newline="") as csvfile:
    #we create a variable to call the csv reader method
    csvreader = csv.reader(csvfile, delimiter=",")  
    #read the header.
    csv_header = next(csvfile)
    #print the header
    print(f"header: {csv_header}")
    #read through each row of data after the header.
    for row in csvreader:
        print(row)
#how to count months.     



















    







