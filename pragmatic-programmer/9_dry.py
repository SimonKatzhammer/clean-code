# old code: 

def print_balance(account)
printf "Debits: %10.2f\n", account.debits
printf "Credits: %10.2f\n", account.credits
if account.fees < 0
printf "Fees: %10.2f-\n", -account.fees
else
printf "Fees: %10.2f\n", account.fees
end
printf " ———-\n"
if account.balance < 0
printf "Balance: %10.2f-\n", -account.balance
else
printf "Balance: %10.2f\n", account.balance
end
end