from bank_cls import Bank

print('Welcome in a bank application.')
print(' ')
in_account_number = int(input('Enter a account number: '))
in_owner_name = str(input('Enter a name of a owner: '))

account = Bank(account_number = in_account_number, owner_name = in_owner_name)

account.deposit(int(input('Enter how many money do you want to deposit: ')))
account.withdraw(int(input('Enter how many money do you want to withdraw: ')))
account.get_balance()