#access and import CSV

import os
import csv

# Specify the correct file path based on the given directory structure
# desktop_path = os.path.expanduser("~/Desktop")
# module_path = os.path.join(desktop_path, "Python_Challenge")
# pybank_path = os.path.join(module_path, "pybank")
pybank_csv = os.path.join("Resources", "budget_data.csv")

# Open and read the CSV file

with open(pybank_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
        
    total_months = 0
    total_profit = 0
    greatest_increase = -99999999
    greatest_decrease = 999999999
    first_row = True
    total_change = 0
    prev_profit=0
    current_change = 0 
    greatest_decrease_date=""
    greatest_increase_date = ""
    
    next(csv_reader)
    for row in csv_reader:
        #skip the header
        total_months +=1
        current_profit =int(row[1])
        total_profit += current_profit
        
        #to do: skip change for 1st rows
        if first_row:
            first_row = False
        else: 
            current_change =current_profit - prev_profit 
            total_change+=current_change
            
            if current_change > greatest_increase:
                greatest_increase = current_change
                greatest_increase_date = row[0]
            if  current_change < greatest_decrease:
                greatest_decrease = current_change
                greatest_decrease_date = row[0]  
                
        #prepare for next row
        prev_profit= current_profit
        

        #average of changes
    average_change = (total_change/ (total_months-1))
    
        
print ("Financial Analysis")
print ('----------------------------')
print (f"Total Months: {total_months}")
print (f"Total: ${total_profit}")
print (f"Average Change:  {round(average_change,2)}")
print (f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    
output_file = os.path.join("results.txt")
with open(output_file, 'w') as text_file:
    
    text_file.write("Financial Analysis\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    
    text_file.write(f"Total: ${total_profit}\n")
    text_file.write(f"Average Change:  {round(average_change,2)}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")