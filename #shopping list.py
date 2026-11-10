#shopping list

shopping_list = []
while True:
    print("\n1 add, 2 remove, 3 show, 4 clear, 0 quit")
    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        item = input("Item: ").strip().lower()
        if item and item not in shopping_list:
            shopping_list.append(item)
    elif choice == "2":
        item = input("Item: ").strip().lower()
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Not in the list")
    elif choice == "3":
        for i, item in enumerate(sorted(shopping_list), 1):
            print(f"{i}. {item}")
    elif choice == "4":
        shopping_list.clear()
    elif choice == "0":
        break