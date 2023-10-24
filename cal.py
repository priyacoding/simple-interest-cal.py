#Calculation of Simple Interest.
def calculate_simple_interest(P, R, T):
    return(P*T*R)/100 

# P = Priciple amount
# R = Interest rate
# T = Time

P, R, T = map(float, input().split()) #Three values dre givenas the input. Values correspond to Priciple amount, Interest rate, Time in that particular order. separated by space

simple_interest = calculate_simple_interest(P, R, T)
print(simple_interest)
