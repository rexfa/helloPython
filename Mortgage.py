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
        return (P*n ,P*n-A*n,A*n-A)

mr = MathRate(100000,2000,12)
print(mr.getRate())


