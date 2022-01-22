# nlantau, 2021-10-10
filter_list=lambda a:[*filter(lambda e:isinstance(e,int),a)]

print(filter_list([1,2,'a']))
