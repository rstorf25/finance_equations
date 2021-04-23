###Future Value of an Ordinary Annuity
### The time value of money is also an important
# concept for the future value of an annuity,
# or the worth of your payments down the line.

###Variables###
# fv = future value
# pmt = payment
# r = interest rate 5% = .05
# t = number of payments 12 = 1 year

pmt = 1000
r = .05
t = 5

def future_value_annunity(pmt,r,t):
    fv = pmt * ((((1 + r) ** t) - 1) / r)
    rounded = round(fv, 2)
    fv = rounded
    return fv

testfv = future_value_annunity(pmt,r,t)
print(testfv)