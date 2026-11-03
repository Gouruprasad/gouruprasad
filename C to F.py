direction = input("Convert to (C/F): ").upper()
temp = float(input("Temperature: "))
if direction == "F":
    f = temp * 9 / 5 + 32
    print(f"{temp:.1f}°C = {f:.1f}°F")
elif direction == "C":
    c = (temp - 32) * 5 / 9
    print(f"{temp:.1f}°F = {c:.1f}°C")
else:
    print("Unknown direction")
