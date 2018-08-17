#计算预付利息的实际年利率,名义本金，实际利息
def interestPrepayment(namedPrincipal ,interest):
    print('名义利率',interest/namedPrincipal)
    monthlyRepayment = namedPrincipal/12
    actualLoan = namedPrincipal - interest
    print('实际年利率',monthlyInterest(monthlyRepayment,actualLoan))


#每月利率，每月还款，名义本金 ,实际利息
def monthlyInterest(monthlyRepayment,namedPrincipal,interest):
    #实际贷款
    actualLoan = namedPrincipal-interest
    m = monthlyRepayment/actualLoan


    
    x=(y-1)*12
    return x


interestPrepayment(120000,14430)
