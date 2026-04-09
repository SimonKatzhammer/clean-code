# old code:

def print_balance(account)
    printf "Debits:  %10.2f\n", account.debits
    printf "Credits: %10.2f\n", account.credits
    if account.fees < 0
        printf "Fees:    %10.2f-\n", -account.fees
    else
        printf "Fees:    %10.2f\n", account.fees
    end
    printf "         ———-\n"
    if account.balance < 0
        printf "Balance: %10.2f-\n", -account.balance
    else
        printf "Balance: %10.2f\n", account.balance
    end
end


# first convert code to python: 
def print_balance(account):
    print("Debits:  %10.2f\n", account.debits)
    print("Credits: %10.2f\n", account.credits)
  if account.fees < 0:
    print("Fees:    %10.2f-\n", -account.fees)
  else:
    print("Fees:    %10.2f\n", account.fees)
    print("         ———-\n")
  if account.balance < 0:
    print("Balance: %10.2f-\n", -account.balance)
  else:
    print("Balance: %10.2f\n", account.balance)


# second extract a funcion out of the function.
def print_balance(account):
  print("Debits:  %10.2f\n", account.debits)
  print("Credits: %10.2f\n", account.credits)
  print_account_info(account.fees, "Fees")
  print("         ———-\n")
  print_account_info(account.balance, "Balance")

def print_account_info(account_info, subject):
  if account_info < 0:
    print(subject + ":    %10.2f-\n", -account_info)
  else:
    print(subject + ":    %10.2f\n", account_info)

# third rework with claude feedback:
def print_balance(account):
  print(f"Debits:  {account.debits:10.2f}\n")
  print(f"Credits: {account.credits:10.2f}\n")
  print_account_info(account.fees, "Fees")
  print("         ———-\n")
  print_account_info(account.balance, "Balance")

def print_account_info(account_info, subject):
  if account_info < 0:
    print(subject + f":    {-account_info:10.2f}-\n")
  else:
    print(subject + f":    {account_info:10.2f}\n")