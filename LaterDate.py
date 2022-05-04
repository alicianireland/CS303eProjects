# File: LaterDate.py
# Description: Program that finds new date after a given number of days. 
# Assignment Number: 4
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
# Slip days used this assignment: 0
#
# On my honor, Alicia Ireland, this programming assignment is my own work
# and I have not provided this code to any other student.


# Program to determine the new date after skipping a given number of days.
def main():
    print("This program asks for a date and days to skip.")
    print("It then displays the date that many days after the given date.")
    print()
    
    # Get current month, year, date and number of days to skip from user.
    month = str(input("Enter the month: "))
    day = int(input("Enter the day of the month: "))
    year = int(input("Enter the year: "))
    print()
    days_to_skip = int(input("Enter the number of days to skip: "))
    # Calculate the new day and save original date for output.      
    new_day = day + days_to_skip
    original_month = month
    original_year = year
    
    #Calculate the new month and day if new day is in the next month.
    if month == "February":
        # Calculate if the year is a leap year or not for February.
        if (year % 4 == 0 and year % 100 != 0): 
            if new_day > 29:
                new_day = (new_day - 29)
                month = "March"
        else:
            if new_day > 28:
                new_day = (new_day - 28)
                month = "March"
    # Calculate new date for months with 30 days.          
    elif month == "April" or month == "September" or month == "June" \
         or month == "November":
        if new_day > 30:
            new_day = (new_day - 30)
            if month == "April":
                month = "May"
            elif month == "September":
                month = "October"
            elif month == "June":
                month = "July"
            elif month == "November":
                month = "December"
    # Calculate new date for months with 31 days.    
    else:
        if new_day > 31:
            new_day = (new_day - 31)
            if month == "January":
                month = "February"
            elif month == "March":
                month = "April"
            elif month == "May":
                month = "June"
            elif month == "July":
                month = "August"
            elif month == "August":
                month = "September"
            elif month == "October":
                month = "November"
            elif month == "December":
                month = "January"
                # Calculate new year for going from December to January.
                year = year + 1                
    
    print()
    # Print out new date and format depending on number of days skipped.
    if days_to_skip == 1:
        print(days_to_skip, "day after", original_month,
              str(day) + ",", original_year, "is", month,str(new_day)
              + ",", str(year) + ".")
    else:
        print(days_to_skip, "days after", original_month,
              str(day) + ",", original_year, "is", month,str(new_day)
              + ",", str(year) + ".")

        
main()   
             
