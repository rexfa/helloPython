import math
def findPayment(loan,r,m):
    return loan*((r*(1+r)**m)/((r+1)**m-1))

class Mortgage(object):
    def __init__(self,loan,annRate,months):
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan,self.rate,months)
        self.legend = None

    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1]-reduction)

    def getTotalPaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend


class Fixed(Mortgage):
    def __init__(self,loan,r,months):
        Mortgage.__init__(self,loan,r,months)
        self.legend = 'Fixed,' + str(round(r*100,2))+ '%'

class FixedWithPts(Mortgage):
    def __init__(self,loan,r,months,pts):
        Mortgage.__init__(self, loan , r , months)
        self.pts = pts
        self.paid = [loan*(pts/100)]
        self.legend = 'Fixed,' + str(round(r*100,2)) + '%,'\
         + str(pts) + ' points'

class TowRate(Mortgage):
    def __init__(self,loan ,r,months,teaserRate,teaserMonths):
        Mortgage.__init__(self,loan,teaserRate,months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12
        self.legend = str(teaserRate*100)\
        +'% for' +str(self.teaserMonths)\
        +' months, then ' + str(round(r*100,2))+'%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths+1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1],self.rate,self.months-self.teaserMonths)
        Mortgage.makePayment(self)
#Ｐ＝Ａ〔（1＋i）n－１〕／〔i（1＋i）n〕 Ｐ為代款金額，Ａ為每期償還金額，i為每期利率，n為期數
class MathRate(Mortgage):
    def __init__(self, loan, fee, months):
        self.months = months
        self.loan = loan
        self.fee = fee
    def getRate(self):
        P = self.loan - self.fee
        A = self.loan/self.months
        n = self.months
        #Pni +Pn *i^2- Ani = An-A
        a = P*n
        b = P*n-A*n
        c= A-A*n
        aRoot = math.sqrt(a)
        i = b/(2*aRoot)
        cc = i*i-c
        ccRoot = math.sqrt(cc)
        r= (ccRoot- i)/aRoot
        #解一个二元一次方程组获取正实数解，就是年利率
        return (r)
#MathRate 公式不是很理解
#用下面这个年化利率公式算出这个在有费的无息贷款中实际年化利率是
# PA=   P'/（（1+n/2）/12） 
# PA是年化实际利率 P'是名义年利率，就是费用处以贷款总额
# n是还款期数，式子中的12是一年12个月
class ActualInterestRateCalculation(Mortgage):
    def __init__(self, loan, fee, months):
        self.months = months
        self.loan = loan
        self.fee = fee
    def getRat(self):
        PA = (self.fee/self.loan)/(((self.months+1)/2)/12)
        return PA

mr = MathRate(100000,2000,12)
print(mr.getRate())
#mr2 = MathRate(100000,200,12)
#print(mr2.getRate())
ac = ActualInterestRateCalculation(100000,2000,12)
print (ac.getRat())
ac2 = ActualInterestRateCalculation(100000,200,12)
print (ac2.getRat())