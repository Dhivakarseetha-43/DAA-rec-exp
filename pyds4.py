import math

n = int(input("Enter the number of observations: "))

x = []
y = []
yp = []

print("Enter X values:")
for i in range(n):
    x.append(float(input()))

print("Enter Y values:")
for i in range(n):
    y.append(float(input()))

print("Enter Y' (Predicted Y) values:")
for i in range(n):
    yp.append(float(input()))

sum_error = 0

for i in range(n):
    sum_error += (y[i] - yp[i]) ** 2

see = math.sqrt(sum_error / (n - 2))

print("Standard Error of Estimate (SEE) =", round(see, 4))