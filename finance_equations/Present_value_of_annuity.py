### Present Value of an Annuity###
###The present value of an annuity equates a series of
# payments in the future to a lump sum today by using the
# time value of money (inflation)—a dollar today is worth more
# than a dollar tomorrow.

#Example:  Deciding whether to take a pension or lottery prize as an annuity or a lump sum.

###Variables ###
# p = present value of an annuity
# pmt = dollar amount of each annuity payment
# r = interest rate or discount rate
# Number of periods in which payments will be made


def present_value_annuity(pmt, r, n):
    p = (pmt * ((1 - (1 / ((1 + r) ** n))) / r))
    rounded = round(p, 2)
    p = rounded
    return p

#Example
#Assume a person has the opportunity to receive an ordinary
# annuity that pays $50,000 per year for the next 25 years,
# with a 6% discount rate, or take a $650,000 lump-sum payment.
# Which is the better option?
pmt = 50000
r = .06
n = 25

testpva = present_value_annuity(pmt, r, n)
print(testpva)
