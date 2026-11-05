
hours1 = int(input("Enter hours for time 1: "))
minutes1 = int(input("Enter minutes for time 1: "))


hours2 = int(input("Enter hours for time 2: "))
minutes2 = int(input("Enter minutes for time 2: "))


total_hours = hours1 + hours2
total_minutes = minutes1 + minutes2


total_hours = total_hours + total_minutes // 60
total_minutes = total_minutes % 60


print("Total time:", total_hours, "hours and", total_minutes, "minutes")