def main():
    pounds = pounds_to_float("£" + input("How much was the meal?: £ "))
    percent = percent_to_float(input("What percentage would you like to charge? " + "%"))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")
    # .2f is an f string argument meaning 2 d.

def pounds_to_float(d):
    print(d)
    # Remove the £, return the number as 
    # a floating point number to 2.d.p
    d = round(float(d.replace('£', '')), 2)
    return d 

def percent_to_float(p):
    print(p)
    # strip % from the string
    # convert the string to a float
    # convert the float into a percentage multiplier
    p = round((float(p.replace('%', ''))/100), 2)
    return p 
#random useless comment
main()
