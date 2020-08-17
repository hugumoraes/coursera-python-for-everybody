score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Score must be a number")

if s < 0.0 and s > 1.0:
    print("Score must be between 0 and 1")
else:
    if s < 0.6:
        print("F")
    elif s < 0.7:
        print("D")
    elif s < 0.8:
        print("C")
    elif s < 0.9:
        print("B")
    else:
        print("A")
