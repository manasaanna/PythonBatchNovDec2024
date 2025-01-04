# Shw the schedule de[ending on the days of the week 
#
#
#

# week_of_day = "Monday"
week_of_day = input("Enter week of the day:").strip().title()

# Method 1
if week_of_day == "Monday":
    print("TIMINGS: 9 AM to 6 PM")
elif week_of_day == "Tuesday":
    print("TIMINGS: 9 AM to 6 PM")
elif week_of_day == "Wednesday":
    print("TIMINGS: 9 AM to 6 PM")
elif week_of_day == "Thursday":
    print("TIMINGS: 9 AM to 6 PM")
elif week_of_day == "Friday":
    print("TIMINGS: 9 AM to 6 PM")
elif week_of_day == "Saturday":
    print("TIMINGS: 9 AM to 1 PM")
elif week_of_day == "Sunday": # or week_of_day == "sunday" or or week_of_day
    print(" ---- HOLIDAY------ ")
else:
    print("INVALID ENTRY! PLEASE TRY AGAIN !! ")

