prices = [12.5, 8.0, 30.0]
with_tax = [round(p * 1.2, 2) for p in prices]
#for p in prices, Take each price p from the prices list
#round(p * 1.2, 2), apply this transformation/math to it
print(with_tax)
