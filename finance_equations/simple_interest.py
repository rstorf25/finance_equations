#Variables
# p = principal
#r = annual interest rate
# t = number of pay periods

def simple_interest(p,r,t):
    si = p*(1+((r/12*t)))
    round = round(si,2)
    si = round
    return si

#Example use
# p = $1000, r = .045 or 4.5% Annual, t = 36 months
testsi = simple_interest(1000,.045,36)
print(testsi)

