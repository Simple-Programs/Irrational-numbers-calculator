fibonacci = [1, 1]
storer1 = 0
storer2 = 0
result = 0
phi = 0
for q in range(1, 100_000):
    storer1 = fibonacci[-2]
    storer2 = fibonacci[-1]
    result += storer1 + storer2
    fibonacci.append(result)
    storer1 = 0
    storer2 = 0
    result = 0

phi = fibonacci[-1] / fibonacci[-2]

print("The formula for calculating pi is 1,1,2,3,5,8,etc,etc. and divide the last term by the second last term")
print("Phi is:", phi)
print("Square of phi:", phi * phi)
print("##########THANK YOU FOR USING MY PHI CALCULATOR!##########")

