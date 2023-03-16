Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Import necessary libraries
... import os
... import csv
... 
... # Set the path for the budget data file
... budget_data_csv = os.path.join("PyBank","Resources", "budget_data.csv")
... 
... # Initialize variables
... total_months = 0
... net_total_amount = 0
... changes_in_profit_losses = []
... previous_profit_loss = 0
... greatest_increase_in_profits = {"date": "", "amount": 0}
... greatest_decrease_in_profits = {"date": "", "amount": 0}
... 
... # Read the budget data file and loop through the rows
... with open(budget_data_csv, "r") as csvfile:
...     csvreader = csv.reader(csvfile, delimiter=",")
...     
...     # Skip the header row
...     next(csvreader)
...     
...     # Loop through the rows
...     for row in csvreader:
...         # Increment the total number of months
...         total_months += 1
...         
...         # Add the current profit/loss to the net total amount
...         current_profit_loss = int(row[1])
...         net_total_amount += current_profit_loss
...         
...         # Calculate the change in profit/loss from the previous month
...         if total_months > 1:
...             current_change = current_profit_loss - previous_profit_loss
...             changes_in_profit_losses.append(current_change)
...             
...             # Check if the current change is the greatest increase or decrease in profits
            if current_change > greatest_increase_in_profits["amount"]:
                greatest_increase_in_profits["date"] = row[0]
                greatest_increase_in_profits["amount"] = current_change
            elif current_change < greatest_decrease_in_profits["amount"]:
                greatest_decrease_in_profits["date"] = row[0]
                greatest_decrease_in_profits["amount"] = current_change
        
        # Set the previous profit/loss to the current profit/loss for the next iteration
        previous_profit_loss = current_profit_loss

# Calculate the average change in profit/loss
average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

# Print the analysis to the terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_in_profits['date']} (${greatest_increase_in_profits['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease_in_profits['date']} (${greatest_decrease_in_profits['amount']})")

# Set the path for the output file
output_file = os.path.join("PyBank","Analysis", "financial_analysis.txt")

# Export the analysis to a text file
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_in_profits['date']} (${greatest_increase_in_profits['amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_in_profits['date']} (${greatest_decrease_in_profits['amount']})\n")

