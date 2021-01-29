# nlantau, 2021-01-29

# Sample input: 1 2 3 4 5
# Sample output: 10 14

arr = [1,3,5,7,9]

def miniMaxSum(arr):
    arr.sort()
    mis = sum(arr[:len(arr)-1:])
    mas = sum(arr[1:])
    print(f"{mis} {mas}")

miniMaxSum(arr)
