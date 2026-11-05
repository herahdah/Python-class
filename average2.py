avg = (e + r + g) / 5
if avg > e and avg > r and avg > g:
    print("higher than all three")
elif avg > e and avg > r:
    print("higher than e, r")

elif avg > e:
    print("just higher than e")
else:
    print("invalid input")