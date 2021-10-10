# nlantau, 2021-10-10
"""
quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
"""
a="How can mirrors be real if our eyes aren't real"

to_jaden_case=lambda a:' '.join(w[0].upper()+w[1:] for w in a.split())

print(to_jaden_case(a))
