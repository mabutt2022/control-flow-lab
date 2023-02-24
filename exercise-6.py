# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
month = input('Enter the month of the year (Jan - Dec): ')
day = int(input('Enter the day of the month: '))

if month.lower() in ['jan', 'feb'] or (day >= 21 and month == 'dec') or (day <= 19  and month == 'mar'):
    print(f'{month} {str(day)} is in Winter')
elif month.lower() in ['apr', 'may'] or (day >= 20 and month == 'mar') or (day <= 20  and month == 'jun'):
    print(f'{month} {str(day)} is in Spring')
elif month.lower() in ['jul', 'aug'] or (day >= 21 and month == 'jun') or (day <= 21  and month == 'sep'):
    print(f'{month} {str(day)} is in Summer')
elif month.lower() in ['oct', 'nov'] or (day >= 22 and month == 'sep') or (day <= 20  and month == 'dec'):
    print(f'{month} {str(day)} is in Fall')