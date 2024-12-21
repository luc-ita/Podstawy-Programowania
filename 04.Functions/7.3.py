import month_select

selected = int(input("Enter the month's number: "))
month_name = month_select.MonthByNumber(selected)
print(f'The name of month {selected} is {month_name}')