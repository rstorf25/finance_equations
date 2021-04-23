###Variables###
# p = principal
# r = interest rate annual
# n = compoundings per period example monthly = 12
# t = number of periods = Number of years in the future

###What is Compound Interest?###
# The compound interest is the interest earned
# on the principal, and any interest accrued
# in the past.

def compound_interest(p,r,n,t):
    ci = p*(1+(r/n))**(n*t)
    rounded = round(ci,2)
    ci = rounded
    return ci

testci = compound_interest(10000,.045,12,7.5)
print(testci)