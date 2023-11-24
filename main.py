from Bank import Bank

bank = Bank()

while True:
    print('Welcome to the bank!')
    print('Please select an option:')
    print('1. Create an account')
    print('2. Make a deposit')
    print('3. Make a withdrawal')
    print('4. Transfer funds')
    print('5. Check balance')
    print('0. Exit')
    choice = input('Enter your choice: ')

    if choice == '1':
        bank.create_account()
    elif choice == '2':
        bank.deposit()
    elif choice == '3':
        bank.withdraw()
    elif choice == '4':
        bank.transfer()
    elif choice == '5':
        bank.get_balance()
    elif choice == '0':
        bank.save_to_file()
        break
    else:
        print('Invalid choice, please try again.')