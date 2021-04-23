###Compounding Annual Growth Rate###
###As the economy moves up and down,
# so do investors' returns. To determine your yearly
# growth rate over several years on an investment,
# use the compound annual growth rate, CAGR.

#Think of CAGR as the rate an investment would
# grow if the rate were constant.

#Variables#
#carg = Compound Annual Growth Rate
#ev = Ending Value
#bv = Beginning Value
# n = number of years

def CAGR(ev,bv,n):
    cagr = ((ev/bv)**(1/n)) - 1
    return cagr

def CAGR_percent(ev,bv,n):
    cagr = ((ev / bv) ** (1 / n)) - 1
    percent = cagr *100
    cagr = percent
    rounded = round(cagr,2)
    cagr = rounded
    return cagr

testcagr = CAGR(19000,10000,3)
print(testcagr)

testperc= CAGR_percent(19000,10000,3)
print(testperc)

