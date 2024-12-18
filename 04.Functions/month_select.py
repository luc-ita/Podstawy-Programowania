month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def MonthByNumber(selected):
    return month_dict[selected]

if __name__ == "__main__":
    # This block will only execute when the script is run directly
    selected = 10
    print(MonthByNumber(selected))