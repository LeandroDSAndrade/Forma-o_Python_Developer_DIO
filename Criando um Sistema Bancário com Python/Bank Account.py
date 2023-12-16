# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato
menu = '''
Type [1] to deposit
Type [2] to withdrawal
Type [3] to see credit report
Type [4] to quit
'''

balance = 0
limit = 500
credit_report = " "
withdrawal_quantity = 0
WITHDRAWAL_LIMIT = 3

while True:

    option = int(input(menu))

    if option == 1:
        value = float(input("How much do you want to deposit?"))

        if value > 0:
            balance += value
            credit_report += f"Deposit: $ {value:.2f}\n"
        else:
            print("invalid value!")
    elif option == 2:
        value = float(input("How much do you want to take?"))

        balance_exceeded = value > balance

        limit_exceeded = value > limit

        withdrawal_exceeded = withdrawal_quantity >= WITHDRAWAL_LIMIT

        if balance_exceeded:
            print("fail: insufficient balance")
        elif limit_exceeded:
            print("fail: the withdrawal amount exceeded the balance ")
        elif withdrawal_exceeded:
            print("fail: number of withdrawals exceeded")
        elif value > 0:
            balance -= value
            credit_report += f"Withdrawal: $ {value:.2f}\n"
            withdrawal_quantity += 1
        else:
            print("fail: invalid value!")

    elif option == 3:
        print("\n=====================EXTRATO=======================")
        print("Não foram realizadas movimentações" if not credit_report else credit_report)
        print(f"\nBalance: R$ {balance:.2f}")
        print("======================================================")
    elif option == 4:
        break
    else:
        print("Type a valid option")
