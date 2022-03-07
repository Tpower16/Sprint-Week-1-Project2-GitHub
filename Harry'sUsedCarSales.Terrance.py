# A program to keep track of sales for Harry's Used Car Lot

# Created By: Terrance Power
# Created On: Feb.15/2022


import datetime
while True:
    # Constants
    TAX_RATE = 0.15
    LIC_FEE_S = 75.00
    LIC_FEE_E = 165.00
    TRAN_FEE = 0.01
    LUX_TAX = 0.016

    print()
    # Gather input from user
    while True:
        InvDate = input("Please Enter The Invoice Date (ie: YYYY-MM-DD): ")
        if InvDate == "":
            print("(Invoice Date Cannot Be Blank - Please Re-enter -)")
        elif len(InvDate) != 10:
            print("(Invoice Date Must Contain 10 Characters - Please Re-enter -)")
        else:
            break

    while True:
        AllowChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        FstName = input("Please Enter Your First Name: ").title()
        if FstName == "":
            print("(First Name Cannot Be Blank - Please Re-enter -)")
        elif set(FstName).issubset(AllowChar) == False:
            print("(First Name Must Contain Valid Characters - Please Re-enter -)")
        else:
            break

    while True:
        AllowChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        LstName = input("Please Enter Your Last Name: ").title()
        if LstName == "":
            print("(Last Name Cannot Be Blank - Please Re-enter -)")
        elif set(LstName).issubset(AllowChar) == False:
            print("(Last Name Must Contain Valid Characters - Please Re-enter -)")
        else:
            break

    while True:
        AllowCharST = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 1234567890-.,'")
        StAdd = input("Please Enter Your Residing Street Address: ").title()
        if StAdd == "":
            print("(Street Address Cannot Be Blank - Please Re-enter -)")
        elif set(StAdd).issubset(AllowCharST) == False:
            print("(Street Address Must Contain Valid Characters - Please Re-enter -)")
        else:
            break

    while True:
        AllowCharC = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")
        City = input("Please Enter Your Residing City: ").title()
        if City == "":
            print("(City Cannot Be Blank - Please Re-enter -)")
        elif set(City).issubset(AllowCharC) == False:
            print("(City Must Contain Valid Characters - Please Re-enter -)")
        else:
            break

    while True:
        AllowCharProv = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")
        Prov = input("Please Enter Your Residing Province (ie: NL, NS, NB): ").upper()
        if Prov == "":
            print("(Province Cannot Be Blank - Please Re-enter -)")
        elif set(Prov).issubset(AllowCharProv) == False:
            print("(Province Must Contain Valid Characters - Please Re-enter -)")
        elif len(Prov) != 3 and len(Prov) != 2:
            print("(Province Must Contain Only 2 Or 3 Characters - Please Re-enter -)")
        else:
            break

    while True:
        Allow_Char_Plt = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        PostCode = input("Please Enter Your Postal Code: ").upper()
        if PostCode == False:
            print("(Postal Code Cannot Be Blank - Please Re-enter -)")
        elif set(PostCode).issubset(Allow_Char_Plt) == False:
            print("(Postal Code Must Contain Valid Characters - Please Re-enter -)")
        elif len(PostCode) != 6:
            print("Postal Code Must Contain Only 6 Characters - Please Re-enter -)")
        else:
            break

    while True:
        Allow_Char_Num = set("0123456789")
        PhnNum = input("Please Enter Your Phone Number (Must be 10 digits): ")
        if PhnNum == "":
            print("(Phone Number Cannot Be Blank - Please Re-enter -)")
        elif set(PhnNum).issubset(Allow_Char_Num) == False:
            print("(Phone Number Cannot Contain Invalid Characters - Please Re-enter -)")
        elif len(PhnNum) != 10:
            print("(Phone Number Must Be 10 Digits - Please Re-enter -)")
        else:
            break

    while True:
        Allow_Char_Plt = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
        PltNum = input("Please Enter Your Plate Number (ie: XXX999): ").upper()
        if PltNum == "":
            print("(Plate Number Cannot Be Blank - Please Re-enter -)")
        elif PltNum[0:3].isalpha() == False:
            print("(First 3 Characters Must Be Letters - Please Re-enter -)")
        elif PltNum[3:6].isdigit() == False:
            print("(Last 3 Characters Must Be Digits - Please Re-enter -) ")
        elif len(PltNum) != 6:
            print("(Plate Number Must Be 6 Characters - Please Re-enter -)")
        else:
            break

    while True:
        CarMake = input("Please Enter The Car Make (ie: Toyota): ").title()
        if CarMake == "":
            print("(Car Make Cannot Be Blank - Please Re-enter -)")
        else:
            break

    while True:
        CarModel = input("Please Enter The Car Model (ie: Corolla): ").title()
        if CarModel == "":
            print("(Car Model Cannot Be Blank - Please Re-enter -)")
        else:
            break

    while True:
        YrOfCar = input("Please Enter The Year Car Was Manufactured (ie: 2018): ")
        if YrOfCar == "":
            print("(Year Car Manufactured Cannot Be Blank - Please Re-enter -)")
        elif set(YrOfCar).issubset(Allow_Char_Num) == False:
            print("(Year Car Manufactured Must Contain Valid Characters - Please Re-enter -)")
        else:
            break

    while True:
        try:
            CarSellPrce = float(input("Please Enter Sale Price Of Car (Must Not Exceed $50,000.00): "))
        except:
            print("(Car Sale Price Must Be A Valid Number - Please Re-enter -)")
        else:
            if CarSellPrce > 50000.00:
                print("(Car Sale Price Must Not Exceed $50,000.00 - Please Re-enter -)")
            else:
                break

    while True:
        try:
            AmtTrdIn = float(input("Please Enter Amount Of Trade In (Must Not Exceed Car Sale Price): "))
        except:
            print("(Trade In Amount Must Be A Valid Number - Please Re-enter -)")
        else:
            if AmtTrdIn > CarSellPrce:
                print("(Trade In Amount Must Not Exceed Car Sale Price - Please Re-enter -)")
            elif AmtTrdIn == "":
                print("(Trade In Amount Cannot Be Blank - Please Re-enter -)")
            else:
                break

    while True:
        AllowChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        SalePrsnName = input("Please Enter The Salespersons Name: ")
        if SalePrsnName == "":
            print("(Salespersons Name Cannot Be Blank - Please Re-enter -)")
        elif set(SalePrsnName).issubset(AllowChar) == False:
            print("(Salespersons Name Must Contain Valid Characters - Please Re-enter -) ")
        else:
            break

    while True:
        CredCardNum = input("Please Enter Your Credit Card Number (ie: 9999999999999999): ")
        if CredCardNum == "":
            print("(Credit Card Number Cannot Be Blank - Please Re-enter -)")
        elif CredCardNum.isdigit() == False:
            print("(Credit Card Number Must Contain Valid Characters - Please Re-enter -)")
        elif len(CredCardNum) != 16:
            print("(Credit Card Number Must Contain 16 Characters - Please Re-enter -)")
        else:
            break

    while True:
        CredChar = set("0123456789/")
        CredExp = input("Please Enter Credit Card Expiry Date (ie: MM/YY): ")
        if CredExp == "":
            print("(Credit Card Expiry Date Cannot Be Blank - Please Re-enter -)")
        elif set(CredExp).issubset(CredChar) == False:
            print("(Credit Card Expiry Must Contain Valid Characters - Please Re-enter -)")
        elif len(CredExp) != 5:
            print("(Credit Card Expiry Must Contain 5 Characters - Please Re-enter -) ")
        else:
            break

    PrceAfTrde = CarSellPrce - AmtTrdIn
    HST = CarSellPrce * TAX_RATE
    TranFee = CarSellPrce * TRAN_FEE
    LuxTax = CarSellPrce * LUX_TAX
    LicFee = LIC_FEE_S
    if PrceAfTrde > 5000.00:
        LicFee = LIC_FEE_E
    if CarSellPrce > 20000.00:
        TranFee = (CarSellPrce * TRAN_FEE) + LuxTax

    TotSalePrce = PrceAfTrde + HST + LicFee + TranFee

    print()
    print("# Years     # Payments     Financing Fee     Total Price     Monthly Payment")
    print("----------------------------------------------------------------------------")
    for Years in range(1, 5):
        NumMonthPay = Years * 12
        FinFee = Years * 39.99
        TotPrce = TotSalePrce + FinFee
        MontPay = TotPrce / NumMonthPay
        TotPrceDSP = "${:,.2f}".format(TotPrce)
        FinFeeDSP = "${:,.2f}".format(FinFee)
        MontPayDSP = "${:,.2f}".format(MontPay)
        print("    {:<1}            {:<2}            {:>7}        {:>10}          {:>9}".format(Years, NumMonthPay,
                                                                                                FinFeeDSP, TotPrceDSP,
                                                                                                MontPayDSP))
    print()

    while True:
        try:
            Choice = int(input("Please Enter Payment Method Must Be Between (1 - 4): "))
        except:
            print("(Payment Method Invalid - Please Re-enter - )")
        else:
            if Choice == "":
                print("(Payment Method Cannot Be Blank - Please Re-enter -)")
            elif Choice < 1 or Choice > 4:
                print("(Payment Method Must Be Between (1 - 4) - Please Re-enter -)")
            else:
                break


    InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
    ReciNo = FstName[0] + "." + LstName[0] + "-" + PltNum[3:6] + "-" + PhnNum[6:10]
    Address = City + "," + "" + Prov + "," + "" + PostCode
    CarDet = YrOfCar + " " + CarMake + " " + CarModel
    CarSellPrceDSP = "${:,.2f}".format(CarSellPrce)
    AmtTrdInDSP = "${:,.2f}".format(AmtTrdIn)
    PrceAfTrdeDSP = "${:,.2f}".format(PrceAfTrde)
    HSTDSP = "${:,.2f}".format(HST)
    LicFeeDSP = "${:,.2f}".format(LicFee)
    TranFeeDSP = "${:,.2f}".format(TranFee)
    TotSalePrceDSP = "${:,.2f}".format(TotSalePrce)
    FstPayDate = InvDate + datetime.timedelta(days = 30)
    if Choice == 1:
        Terms = 1
        TotNumPay = 12
        MthlyPay = (TotSalePrce + 39.99) / 12
    elif Choice == 2:
        Terms = 2
        TotNumPay = 24
        MthlyPay = (TotSalePrce + 79.98) / 24
    elif Choice == 3:
        Terms = 3
        TotNumPay = 36
        MthlyPay = (TotSalePrce + 119.97) / 36
    elif Choice == 4:
        Terms = 4
        TotNumPay = 48
        MthlyPay = (TotSalePrce + 159.96) / 48
    else:
        break
    MthlyPayDSP = "${:,.2f}".format(MthlyPay)
    while True:
        print()
        print("     Honest Harry Car Sales")
        print("    Used Car Sale and Receipt")
        print()
        print("Invoice Date:", InvDate.strftime("%B %d, %Y"))
        print("Receipt No:", ReciNo)
        print()
        print("Sold to:")
        print("    ", FstName[0] + "." + " " + LstName)
        print("     {:<}".format(StAdd))
        print("     {:<}".format(Address))
        print()
        print("Car Details:")
        print("     {:<}".format(CarDet))
        print("----------------------------------")
        print("Sale Price:             {:>10}".format(CarSellPrceDSP))
        print("Trade Allowance:        {:>10}".format(AmtTrdInDSP))
        print("Price After Trade:      {:>10}".format(PrceAfTrdeDSP))
        print("                        ----------")
        print("HST:                    {:>10}".format(HSTDSP))
        print("License Fee:            {:>10}".format(LicFeeDSP))
        print("Transfer Fee:           {:>10}".format(TranFeeDSP))
        print("                        ----------")
        print("Total Sales Cost:       {:>10}".format(TotSalePrceDSP))
        print("----------------------------------")
        print("Terms: {:<1}        Total Payments: {:<2}".format(Terms, TotNumPay))
        print("Monthly Payment Date:    {:>9}".format(MthlyPayDSP))
        print("First payment date:","    ", FstPayDate.strftime("%d-%b-%y"))
        print()
        print("     Honest Harry Car Sales")
        print("Best used cars at the best price!")
        break
    print()
    print()

    while True:
        Continue = input("Would You Like To Process Another Claim (Y/N)? ").upper()
        if Continue == "N":
            exit()
        elif Continue == "Y":
            break
    print()

