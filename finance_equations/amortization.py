#Variable Explanation
# p = principal
#r = Annaual Interest Rate
#t = number of pay periods (Months)
# n = payments per period

def monthly_payments(p,r,t,n):
    monthly_rate = r/12
    r = monthly_rate
    top = p * (r/n)
    bottom = (1-(1+(r/n))**(-n*t))
    mp = top / bottom
    round = round(mp,2)
    mp = round
    return mp

#Example Use
mortgage = monthly_payments(200000,.045,360,1)
print(mortgage)
