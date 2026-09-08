# import math

# x = int(input())

# res = 0
# fact = 1
# x_deg = 1

# sign = True

# for i in range(1, 14):
#     fact = fact * i
#     x_deg = x_deg * x

#     # i mod 2
#     if i % 2 == 0:
#         continue
#     else:
#         if sign == True:
#             res = res + (x_deg / fact)
#         else:
#             res = res - (x_deg / fact)

#         sign = not sign

# x = int(input())

# numerator = 1
# denominator = 1

# deg_of_two = 1

# res = 1

# for i in range(1, 7):
#     deg_of_two = deg_of_two * 2
    
#     numerator = numerator * (x - deg_of_two)
#     denominator = denominator * (x - (deg_of_two - 1))

#     res = res * (numerator / denominator)

# print(res)

# import math

# x = int(input())
# n = int(input())

# res = 0

# deg_sin = 1

# for i in range(1, n + 1):
#     deg_sin = deg_sin * math.sin(x)

#     res = res + deg_sin

# print(res)
