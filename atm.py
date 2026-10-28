print("---------wlcm to the mini atm machine-----------")


account={
    "Name":"Yash Patel",
    "account number":464649997,
    "pin":1234,
    "type":"bussiness account",
    "balance":700000000
}

print("please enter your atm card")
atm=int(input("1.already entered\n2.i have no atm"))
if atm==1:
    print("your atm is scaning")


    try:
        pin=int(input("enter your pin:"))

        if pin==account["pin"]:
            print("your pin is correct")
            print("======wlcm to the menu======")
            print("1.check balance:")
            print("2.withdraw money")
            print("3.transfer money")
            print("4.type of account")
            print("5.change pin")
            print("6.exit")

            choice=int(input("enter your choice"))
            if choice==1:
                print("your bank balance is",account["balance"])
            elif choice==2:
                try:
                    money=int(input("enter your withdrawable ammount"))
                    if money>account["balance"]:
                        print("you do not have inofe money to withdraw")
                    else:
                        account["balance"]=account["balance"]-money
                        print("you withdrawed",money,"ruppes")
                        print("so you have",account["balance"],"ruppe in your account") 
                except:
                    print("your money must be in number not in  alphabate")
            elif choice==3:
                try:
                    transfer=int(input("please enter your transfer money"))
                    print("your transfering ammount","=",transfer)
                    account["balance"]=account["balance"]+transfer
                    print("your bank balance is",account["balance"])
                except:
                    print("your debeting money must be in internger")
            elif choice==4:
                print("your account type is",account["type"])
            elif choice==5:
                try:
                    change=int(input("enter your current pin"))
                    if change==account["pin"]:
                        try:
                            new=int(input("enter your new pin"))
                            account["pin"]=new
                            print("your new pin is",account["pin"])
                        except:
                            print("pin is only in numaric so i can not change your pin")
                    else:
                        print("your current pin does not match with your entered pin")
                except:
                    print("pin must be numaric")
            elif choice==6:
                print("just take your atm card")
                        
            else:
                print("enter the correct choice")
        else:
            print("enter your pin correctly")          
    except:
        print("enter pin in numaric")



else :
    print("if you have not atm card so what are doing.just go to the bank and bring your atm")