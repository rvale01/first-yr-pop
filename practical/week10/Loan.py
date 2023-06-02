class Loan:

    def __init__(self, annualInterestRate=2.5, numberOfYears=1, loanAmount=1000):
        self.__annualInterestRate = annualInterestRate
        self.__numberOfYears = numberOfYears
        self.__loanAmount = loanAmount

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getNumberOfYears(self):
        return self.__numberOfYears

    def setNumberOfYears(self, numberOfYears):
        self.__numberOfYears = numberOfYears

    def getLoanAmount(self):
        return self.__loanAmount

    def setLoanAmount(self, loanAmount):
        self.__loanAmount = loanAmount

    def getMonthlyPayment(self):
        if(self.__annualInterestRate<0):
            return "Annual interest rate cannot be less than 0"
        elif(self.__numberOfYears< 0):
            return "Number of years cannot be less than 0"
        elif(self.__loanAmount<0):
            return "Loan amount cannot be less than 0"
        else:
            monthlyInterestRate = self.__annualInterestRate / 1200
            numberOfPayments = self.__numberOfYears*12
            monthlyPayment = self.__loanAmount * monthlyInterestRate * (1 + monthlyInterestRate) * numberOfPayments / ((1 + monthlyInterestRate) * numberOfPayments - 1)
            return monthlyPayment

    def getTotalPayment(self):
        if(type(self.getMonthlyPayment()) == float):
            totalPayment = self.getMonthlyPayment() * self.__numberOfYears * 12
            return totalPayment
        else:
            return self.getMonthlyPayment()


l = Loan(7.5, 30, 100000)
print("Total payment: " + str(l.getTotalPayment()))
m = Loan(-1, 3, 3)
if(type(m.getTotalPayment()) == float):
    print("Total payment: " + str(m.getTotalPayment()))
else:
    print(m.getTotalPayment())
