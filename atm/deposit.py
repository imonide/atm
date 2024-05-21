def deposits (y_balance, new_deposit,swithdraw):
    y_balance += new_deposit
    y_balance -= swithdraw
    print("Your new balance is: ", y_balance)
    return y_balance


