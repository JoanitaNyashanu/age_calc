#import datetime

# Step 1
# Ask the user for their name and the year they were born.
name = input("What's your name: ")
#birth_year = input("What year were you born {}? ".format(name))

while True:
    birth_year = input("What year were you born? ")
    try:
        birth_year = int(birth_year)
    except ValueError:
        continue
    else:
        break


# Step 2
# Calculate and print the year they'll turn 25, 50, 75, and 100.
# current_age = timedelta(......)
# if 25-current_age <= 0 or :
# if

current_year = 2019
current age = current_year - birth_year
turn_25 = (25-current_age) + current_year
turn_50 = (50-current_age) + current_year
turn_75 = (75-current_age) + current_year
turn_100 = (100-current_age) + current_year


# Step 3
# If they're already past any of these ages, skip them.
if turn_25 > current_year:
    print("You'll turn 25 in the year {}, {}".format(turn_25, name))
if turn_25 > current_year:
    print("You'll turn 50 in the year {}, {}".format(turn_50, name))
if turn_25 > current_year:
    print("You'll turn 75 in the year {}, {}".format(turn_75, name))
if turn_25 > current_year:
    print("You'll turn 100 in the year {}, {}".format(turn_100, name))
