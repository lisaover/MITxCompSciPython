#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def calculateBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: balance on account at start
    int_r: annual interest rate
    min_r: minimum monthly payment rate

    returns: remaining balance after one year of paying the minimum 
             monthly payment

    For each month:

    1) Compute the monthly payment, based on the previous month’s balance.
    2) Update the outstanding balance by removing the payment, then charging 
       interest on the result.
    3) Output the month, the minimum monthly payment and the remaining balance.
    4) Keep track of the total amount of paid over all the past months so far.

    Print out the result statement with the total amount paid and the remaining 
    balance.

    '''
    totalPaid = 0
    for i in range(12):
        monthlyPayment = balance*monthlyPaymentRate
        totalPaid = totalPaid + monthlyPayment
        monthlyUnpaid = balance - monthlyPayment
        balance = monthlyUnpaid + monthlyUnpaid*(annualInterestRate/12.0)
        print('Month ' + str(i+1) + ' Remaining balance: ' + str(round(balance,2)))
    print('Remaining balance: ' + str(round(balance,2)))
            
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#calculateBalance(balance, annualInterestRate, monthlyPaymentRate)

'''
Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year, for example:

Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance at the 
end of the month (after the payment for that month is made). The monthly 
payment must be a multiple of $10 and is the same for all months. Notice that 
it is possible for the balance to become negative using this payment scheme, 
which is okay. A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - 
        (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + 
        (Monthly interest rate x Monthly unpaid balance)
'''
balance = 3926
annualInterestRate = 0.2
fixedMonthlyPayment = 0
newBalance = balance
while newBalance > 0:
    fixedMonthlyPayment += 10
    newBalance = balance
    monthlyUnpaid = 0
    for i in range(12):
        monthlyUnpaid = newBalance - fixedMonthlyPayment
        newBalance = monthlyUnpaid + monthlyUnpaid*(annualInterestRate/12.0)
#print('Lowest Payment: ' + str(fixedMonthlyPayment))


'''
    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly payment lower bound = Balance / 12
    Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0

Write a program that uses these bounds and bisection search (for more info 
check out the Wikipedia page on bisection search) to find the smallest monthly 
payment to the cent (no more multiples of $10) such that we can pay off the 
debt within a year. 
'''
'''
ATTEMP PART ONE
balance = 320000
annualInterestRate = 0.2
# set lower and upper bounds for bisection search
lowerBound = balance/12
upperBound = (balance * (1 + annualInterestRate)**12)/12.0
# use bisection to determine first number to check
#fixedMonthlyPayment = (lowerBound + upperBound)//2
newBalance = balance
fixedMonthlyPayment = 0
newBalance = balance
while newBalance != 0:
    newBalance = balance
    monthlyUnpaid = 0
    fixedMonthlyPayment = (lowerBound + upperBound)//2
    for i in range(12):
        monthlyUnpaid = newBalance - fixedMonthlyPayment
        newBalance = monthlyUnpaid + monthlyUnpaid*(annualInterestRate/12.0)
    if abs(newBalance) < 10:
        break
    if newBalance > 0:
        # bisect upper section to determine next number to check
        lowerBound = fixedMonthlyPayment
    elif newBalance < 0:
        # bisect lower section to determine next number to check
        upperBound = fixedMonthlyPayment
print('Lowest Payment: ' + str(fixedMonthlyPayment))
'''
balance = 213543
annualInterestRate = 0.22
# set lower and upper bounds for bisection search
lowerBound = balance/12
upperBound = (balance * (1 + annualInterestRate)**12)/12.0
# use bisection to determine first number to check
#fixedMonthlyPayment = (lowerBound + upperBound)//2
newBalance = balance
fixedMonthlyPayment = 0
newBalance = balance
while True:
    newBalance = balance
    monthlyUnpaid = 0
    fixedMonthlyPayment = (lowerBound + upperBound)//2
    for i in range(12):
        monthlyUnpaid = newBalance - fixedMonthlyPayment
        newBalance = monthlyUnpaid + monthlyUnpaid*(annualInterestRate/12.0)
    if abs(newBalance) < 10:
        break
    if newBalance < 0:
        # bisect lower section to determine next number to check
        upperBound = fixedMonthlyPayment
    else:
        # bisect upper section to determine next number to check
        lowerBound = fixedMonthlyPayment
# if newBalance is greater than zero, increase the payments by 0.01 until 
# just under zero
while newBalance > 0:
    fixedMonthlyPayment += 0.01
    newBalance = balance
    monthlyUnpaid = 0
    for i in range(12):
        monthlyUnpaid = newBalance - fixedMonthlyPayment
        newBalance = monthlyUnpaid + monthlyUnpaid*(annualInterestRate/12.0)
# if newBalance is less than zero, decrease the payments by 0.01 until 
# very close to zero
while newBalance < 0:
    fixedMonthlyPayment -= 0.01
    newBalance = balance
    monthlyUnpaid = 0
    for i in range(12):
        monthlyUnpaid = newBalance - fixedMonthlyPayment
        newBalance = monthlyUnpaid + monthlyUnpaid*(annualInterestRate/12.0)

print('Lowest Payment: ' + str(round(fixedMonthlyPayment, 2)))
