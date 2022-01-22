# nlantau 2021-11-04
"""
1,2,3,4,5,6
1,3,6,10,15,21
"""
sum_triangular_numbers=lambda x:sum([(n*(n+1))//2 for n in range(x+1)])

print(sum_triangular_numbers(4))
