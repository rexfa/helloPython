from Mortgage import *

def compareMortgage(amt,years,fixedRate,pts,ptsRate,varRate1,varRate2,varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt,fixedRate,totMonths)
    fixed2 = FixedWithPts(amt,ptsRate,totMonths,pts)
    towRate = TowRate(amt,varRate2,totMonths,varRate1,varMonths)
    morts = [fixed1,fixed2,towRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
    for m in morts:
        print(m)
        print('Total payments = $' + str(int(m.getTotalPaid())))

compareMortgage(amt=200000,years =30 ,fixedRate=0.07,pts = 3.25,ptsRate=0.05,varRate1=0.045,varRate2=0.095,varMonths = 48)