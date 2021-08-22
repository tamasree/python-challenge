import os
import csv

fpath = os.path.join('PyBank', 'resources', 'budget_data.csv')

months = []
profit_loss = []
changes = []
total = 0
past_profit_or_loss = 0
i = 0

with open(fpath, 'r', newline="") as csv_file:
    csv_read = csv.reader(csv_file)
    next(csv_read)

    for row in csv_read:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        total += int(row[1])

        if (i > 0):
            change = int(row[1])-past_profit_or_loss
            changes.append(change)
       # reset past_profit_or_loss for counting change in next row
        past_profit_or_loss = int(row[1])
        # increase counter for counting change in next row
        i += 1

average_change = sum(changes)/len(changes)

greatest_increase_in_profit = max(profit_loss)

month_of_greatest_increase = months[profit_loss.index(
    greatest_increase_in_profit)]

greatest_decrease_in_profit = min(profit_loss)

month_of_greatest_decrease = months[profit_loss.index(
    greatest_decrease_in_profit)]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"average  Change: ${round(average_change, 2)}")
print(
    f"Greatest Increase in Profits: {month_of_greatest_increase} {greatest_increase_in_profit}")
print(
    f"Greatest Decrease in Profits: {month_of_greatest_decrease}{greatest_decrease_in_profit}")

# printing results in a text file

with open("PyBank_results.txt", 'w+') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {len(months)}\n")
    f.write(f"Total: ${total}")
    f.write(f"average  Change: ${round(average_change, 2)}\n")
    f.write(
        f"Greatest Increase in Profits: {month_of_greatest_increase} {greatest_increase_in_profit}\n")
    f.write(
        f"Greatest Decrease in Profits: {month_of_greatest_decrease}{greatest_decrease_in_profit}\n")
