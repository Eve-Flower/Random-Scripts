import math

x = float(input("enter value: "))
def get_e(value):
    e_val = (float(math.e)**value)
    print(e_val)
    return (e_val)

def get_logOdds(value):
    e_val = (float(math.e)**value)
    p = e_val/(1+e_val)
    print(p)
    return (p)

get_e(x)
get_logOdds(x)
