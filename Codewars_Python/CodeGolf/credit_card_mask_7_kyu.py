# nlantau, 2021-10-10
'''
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''
#a="4556364607935616"
#a="64607935616"
#b="".join([*map(lambda x:'#',a[:-4%len(a) if len(a) > 0 else 0])])
#c=a[-4%len(a) if len(a) > 0 else 0:]

maskify = lambda a:"".join([*map(lambda x:'#',a[:-4%len(a) if len(a) > 4 else 0])])+"".join(a[-4%len(a) if len(a) > 4 else 0:])



#print(b+"".join(c))
print(maskify("123"))
print("#######5616<--expected")


