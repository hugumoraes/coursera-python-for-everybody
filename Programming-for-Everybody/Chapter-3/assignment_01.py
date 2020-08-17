hrs = input("Enter Hours:")  # 45
h = float(hrs)
rate = input("Enter Rate:")  # 10.50
r = float(rate)

if h > 40:
    overH = h - 40
    h = 40

pay = (h * r) + (overH * (r * 1.50))

print(pay)  # 498.75
