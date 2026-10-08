# number = int(input("Enter a number:"))
# result = "even" if number % 2 == 0 else "odd"
# print(f"{number} is {result}")


balance = 10000

while True:
    
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
       
    choice = input("Choose an option: ")
    
    if choice == '1':
        print(f"Your balance is ₦{balance}\n")
        
    elif choice == '2':
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit successful. New balance: ₦{balance}\n")
        
    elif choice == '3':
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds\n")
        else:
            balance -= amount
            print(f"Withdrawal successful. New balance: ₦{balance}\n")
            
    elif choice == '4':
        print("Thank you for banking with us")
        break
        
    else:
        print("Invalid option. Please try again.\n")
    
    