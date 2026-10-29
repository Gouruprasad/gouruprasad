contact = {"guru": ["9514815766", "alloy@gamil.com"]}
name = input("name: ")
phone_number = int(input("number: "))
email = input("email: ")
contact[name] = [phone_number,email]
search = input("search: ")
if search in contact:
     phone_number,email = contact[search]
     print(f"{search}: {phone_number} / {email}")
else:
    print(f"{search} not found)")   
print(len(contact),"contact")
