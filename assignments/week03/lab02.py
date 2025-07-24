
# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")

balance = 1000
pin = "1234"
 
entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            print(f"Your balance is: ${balance}")
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Enter a valid amount!")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance}")
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Enter a valid amount!")
            else:
                balance += amount
                print(f"Deposit successful. New balance: ${balance}")
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")
else:
    print("Invalid PIN")