# nlantau, 2021-10-28

find_uniq=lambda a:[*filter(lambda x:x[1]==1,zip(a,map(lambda x:a.count(x),a)))][0][0]

print(find_uniq([1,1,1,1,1,2,1,1]))
