winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}

def calc_total_hours(semester: dict):
    return sum(semester.values())


print('The total number of hours in the winter semester is ', calc_total_hours(winter_semester))
    
