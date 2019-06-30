import os
import csv

csv_path = os.path.join("budget_data.csv") 
pathout = os.path.join("Financial Results.txt")

with open(csv_path, newline="") as csvfile:  
    reader = csv.reader(csvfile, delimiter=",")

    csv_reader = next(reader)
    profit_loss = []
    total_month = []
    profit_loss_change = []

    for row in reader:
        profit_loss.append(float(row[1]))
        total_month.append(row[0])
    
    #print("Financial Analysis")
    #print("------------------")
    #print("Total Months:", len(total_month))
    #print("Total Profit/Loss: $", sum(profit_loss))

    for i in range(1,len(profit_loss)):
        profit_loss_change.append(profit_loss[i] - profit_loss[i-1])   
        
        avg_profit_loss_change = sum(profit_loss_change)/len(profit_loss_change)

        max_profit_loss_change = max(profit_loss_change)

        min_profit_loss_change = min(profit_loss_change)
        
        max_profit_loss_change_date = str(total_month[profit_loss_change.index(max(profit_loss_change))])
        
        min_profit_loss_change_date = str(total_month[profit_loss_change.index(min(profit_loss_change))])


    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {len(total_month)}")
    print(f"Total Profit/Loss: $ {sum(profit_loss)}")
    print(f"Average Profit/loss Change: $ {round(avg_profit_loss_change)}")
    print(f"Greatest Increase in Profits:{max_profit_loss_change_date} - $ {max_profit_loss_change}")
    print(f"Greatest Decrease in Profits:{min_profit_loss_change_date} - $ {min_profit_loss_change}")

with open(pathout, "w") as txt_file:
    
    txt_file.write("Financial Analysis")
    txt_file.write("-------------------------")
    txt_file.write(f"Total Months: {len(total_month)}")
    txt_file.write(f"Total Profit/Loss: $ {sum(profit_loss)}")
    txt_file.write(f"Greatest Increase in Profits:{max_profit_loss_change_date} - $ {max_profit_loss_change}")
    txt_file.write(f"Greatest Decrease in Profits:{min_profit_loss_change_date} - $ {min_profit_loss_change}")