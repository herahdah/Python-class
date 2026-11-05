
score = float(input("Enter the score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
elif score >= 45:
    print("Grade: D")
elif score >= 40:
    print("Grade: E")
else:
    print("Grade: F")