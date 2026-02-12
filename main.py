# expense Tracker Project

expenseList = [] #list of Expense in form of dictionary

print("Welcome to My expenseTracker Python Priject")

while True:
    print("============MENU============")
    print("1 Add Expense")
    print("2 View Expenses")
    print("3 View Total Spending")
    print("4 Exit")
    print("=============================")

    choice = input("Enter The Value Which Option You Want To Perform:")

    # 1 Add Expense
    if (choice == "1"):
        date = input("Enter date (DD-MM-YY): ")
        category = input("Enter Category On Which You Spend: ")
        description = input("Enter Short Description: ")
        amount = float(input("Enter The Amount (In Rupees): "))
        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }
        expenseList.append(expense)
        print("\n Expense Added Successfully!" )

    # 2 View All Expenses 
    elif (choice == "2") :
        if len(expense) == 0:
            print("\n⚠️ No Expenses Recorded Yet. Pehle Kharcha kar Le Ladle..")
        else : 
            print("\n ----All Expenses----")
            i = 1
            for eachkharcha in expenseList:
                print(f"---Kharcha Number {i}--- ->\n Date:{eachkharcha ["date"]},\n Category:{eachkharcha ["category"]},\n Description:{eachkharcha ["description"]},\n Amount:{eachkharcha ["amount"]} \n\n\n")
                i+=1

    # 3 View Total Spending
    elif (choice == "3") :
        total = 0
        for eachkharcha in expenseList :
            total+= eachkharcha["amount"]

        print("\n Total Kharch =", total)

    # 4 Exit
    elif (choice == "4") :
        print("Bahut Bahut Dhanyawaad Aapka Aapne Humara Use Kia")
        break

    else :
        print("InValid Choice..Try Again")
