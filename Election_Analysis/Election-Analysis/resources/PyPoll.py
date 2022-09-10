#the data we need
#1. The total number of votes cast
#2. A complete list of candidates 
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
import csv

import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("C:\Users\mnorr\OneDrive\Desktop\bootcamp\data and such\Election_Analysis\Election-Analysis\resources")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 initialize a vote counter
total_votes=0


# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: perform analysis.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes+=1

#print the total votes        
print(total_votes)

# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")


# Close the file.
election_data.close()
