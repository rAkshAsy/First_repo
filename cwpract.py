"""
Complete the function which returns the weekday according to the input number:

1 returns "Sunday"
2 returns "Monday"
3 returns "Tuesday"
4 returns "Wednesday"
5 returns "Thursday"
6 returns "Friday"
7 returns "Saturday"
Otherwise returns "Wrong, please enter a number between 1 and 7"
"""



def what_day(num: int): 
    day_lib = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    try:
        print(day_lib[int(num)])
    except KeyError:
        print("Wrong, please enter a number between 1 and 7")
    except  TypeError:
        print("Wrong, please enter a number between 1 and 7")
    except  ValueError:
        print("Wrong, please enter a number between 1 and 7")


def whatDay(num):
        day_lib = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
        return day_lib.get(num, "Wrong, please enter a number between 1 and 7")




print(whatDay(0))
print(whatDay(1))
print(whatDay(3))
print(whatDay(10))
print(whatDay('Hello'))
print('**'*50)

what_day(1)
what_day(3)
what_day(0)
what_day(10)
what_day('Hello')