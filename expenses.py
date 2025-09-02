import csv
import datetime
from datetime import date,datetime
import sys

def main():
    print("Please Type Your Choice")
    ch = int(input("1. Add Expense\n"
          "2. View Expenses\n"
          "3. Delete Expenses\n"
                   "4. Total Expenses of a perticular date\n;"
          ))
    choice(ch)

def values():

    try:
        dates = input("Enter the date: ").strip()
        amount = int(input("Enter the amount: "))
        description = input("Enter the description: ").strip().lower()
        return dates, amount, description
    except ValueError:
        print("Please enter a number.")


def date_check(dates):
    try:
        data = date.fromisoformat(dates)
        return data
    except ValueError:
        print(f"{dates} is not a valid date")
        sys.exit()
def read_csv():
    with open("expenses.csv", 'r', newline='\n') as s:
        reader = csv.DictReader(s)
        return list(reader)

def choice(ch):
    if ch == 1:
        with open("expenses.csv",'a',newline='\n') as s:
            dates,amount,description = values()
            data = date_check(dates)
            sa = csv.DictWriter(s, fieldnames=['date', 'amount', 'description'])
            if data:
                sa.writerow({'date': data, 'amount': amount, 'description': description})
            else:
                sys.exit()
    elif ch == 2:
        all_1 = input("Do you want to view all Expenses? (y/n)").lower()
        ls = read_csv()
        if all_1 == "y":
           for row in ls:
               print(f"{row['date']} {row['amount']} {row['description']}")
        elif all_1 == "n":
            new_opt = int(input("how many days expenses do you want to view?"))
            ls = read_csv()
            for row in ls[:new_opt]:
                print(f"{row['date']} {row['amount']} {row['description']}")
    elif ch == 3:
        provide_s = input("Enter the date you want to remove: ")
        new_value = date_check(provide_s)
        ls = read_csv()
        with open("expenses.csv",'w',newline='\n') as s:
            writer = csv.DictWriter(s, fieldnames=['date', 'amount', 'description'])
            writer.writeheader()
            for r in ls:
                if r['date'] == provide_s:
                    ls.remove(r)
            for r in ls:
                writer.writerow(r)
    elif ch == 4:
        provide_s = input("Enter the date you want total expense for: ")
        new_value = date_check(provide_s)
        ls = read_csv()
        x = 0
        for r in ls:
            if r['date'] == provide_s:
                x += int(r['amount'])

        print(f"the total amout of date is {x}")


    else:
        print("Please enter a valid choice.1,2,3")
        sys.exit()





if __name__ == '__main__':
    main()
