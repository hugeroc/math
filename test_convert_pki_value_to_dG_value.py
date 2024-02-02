import math

pKi_9822 = 6.20797

def pic50_ic50(pic50):
    #convert the pic50 to ic50, return the ic50 in M unit
    return (10.0)**(-pic50)

def ic50_to_dG(ic50):
    #convert the ic50 values to binding affinity
    return math.log(ic50) * 0.5961

ic50_9822 = pic50_ic50(pKi_9822)
dG_9822 = ic50_to_dG(ic50_9822)

print ("pKi_9822", pKi_9822)
print ("ic50_9822", ic50_9822)
print ("dG_9822", dG_9822)
