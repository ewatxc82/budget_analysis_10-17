import csv
import os

file = csvpath = 'budget_data.csv'
file_output = csvpath = 'budget_final.txt'
file = os.path.join('Resources','budget_data.csv')
file_output = os.path.join("budget_final.txt")

#Keeping Track of My Parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000000000]
total_net = 0

with open(file) as budget_data:
      reader = csv.reader(budget_data)

      header = next(reader)

      #Take first row from the net_change_list
      first_row = next(reader)
      total_months =+ 1
      total_net += int(first_row[1])
      prev_net = int(first_row[1])
      
      #Loop to find Total
      for row in reader:
            total_months += 1
            total_net += int(row[1])

            #Include net_change in the loop
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            net_change_list += [net_change]
            month_of_change += [row[0]]

            #If statement to establish greatest_increase
            if net_change > greatest_increase[1]:
                  greatest_increase[0] = row[0]
                  greatest_increase[1] = net_change
            #If statement to calculate greatest_decrease
            if net_change < greatest_decrease[1]:
                  greatest_decrease[0] = row[0]
                  greatest_decrease[1] = net_change

      #Calculates your average net change
      net_monthly_avg = sum(net_change_list) / len(net_change_list)

      output = (
            f"Financial Analysis\n"
            f"----------------------------\n"
            f"Total Months: {total_months}\n"
            f"Total: ${total_net}\n"
            f"Average Change: ${net_monthly_avg: .2f}\n"
            f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
            f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n")

      print(output)

      with open(file_output, "w") as txt_file:
            txt_file.write(output)
      

            
      
