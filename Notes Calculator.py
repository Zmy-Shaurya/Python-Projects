money = int(input("Enter your money(multiples of 10): "))

if money < 10:
    print("Kindly enter more than 10")

else:
    fivehun  = money//500
    money   -= 500*fivehun

    twohun   = money//200
    money   -= 200*twohun

    onehun   = money//100
    money   -= onehun*100

    fifties  = money//50
    money   -= fifties*50

    twenties = money//20
    money   -= twenties*20

    tens     = money//10
    money   -= tens*10

    print("500s -> ",fivehun)
    print("200s -> ",twohun)
    print("100s -> ",onehun)
    print("50s  -> ",fifties)
    print("20s  -> ",twenties)
    print("10s  -> ",tens)
