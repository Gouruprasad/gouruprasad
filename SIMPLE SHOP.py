#SIMPLE SHOP

menu = {
    "Apple": 13,
    "Bread": 28,
    "Milk": 57 }

total = 0

print("Products Menu:")
for item, price in menu.items():
    print(f"- {item}: ${price:.2f}")

while True:
    choice = input("Enter product name to buy (or type 0 to finish): ").strip()
    
    if choice == "0":
        break



    matched_item = None
    for item in menu:
        if item.lower() == choice.lower():
            matched_item = item
            break

    if matched_item:
        total += menu[matched_item]
        print(f"Added {matched_item}. Current total: ${total:.2f}")
    else:
        print("Invalid product, try again.")

if total > 10:
    total = total * 0.90
    print("10% discount applied!")

print(f"Final Total: ${total:.2f}")