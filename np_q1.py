#fahrenheit to celcius
import numpy as np

l=[]
val=list(map(int,input("Enter fanhrenheit values :").split()))

# l=[100,98.4,91.50,99.78,101.5]
fht = np.array(val)

degree = (fht - 32) * (5 / 9)

print("Fahrenheit values:", fht)
print("Centigrade values:", degree)




# degree = np.array([])

# for temp in fht:
#     degreeval = (temp - 32) * (5 / 9)
#     degree = np.append(degree, degreeval)

# print("Fahrenheit values", fht)
# print("Centigrade values", degree)