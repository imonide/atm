def paybill():
        print("choose category \n"
              "1 for Electric bills \n"
              "2 for Waste bill \n"
              "3 for Airtime \n")
        return

def electric_bill(pick):
        if pick == 1 or 2 or 3:
            print("choose your city \n"
                  "1 for BENIN \n"
                  "2 for LAGOS \n"
                  "3 for ABUJA \n")


def benin_bill(pick):
    if pick == 1 or 2 or 3:
        print("write the amount you want to pay")



def pin_verification(pin):
    if pin == 1234:
        print("TRANSACTION IN PROGRESS....")

def bill_pay(w_balance,sbill):
    if sbill > w_balance:
        print("(Insufficient balance please deposit)")
    else:

        w_balance -= sbill
        print("Payment Successful")
        print(f'(your current balance is {w_balance} Naira)')

    return w_balance