-- nlantau, 2021-02-18

{-
Given an array of integers (x), and a target (t),
you must find out if any two consecutive numbers in the array sum to t. 
If so, remove the second number.
Example:
x = [1, 2, 3, 4, 5]
t = 3
1+2 = t, so remove 2. No other pairs = t, so rest of array remains:
[1, 3, 4, 5]
Work through the array from left to right.
Return the resulting array.
-}

trouble :: [Int] -> Int -> [Int]
trouble [] _ = []
trouble [x] _ = [x]
trouble (x:y:xs) n
    | x + y /= n = x : trouble (y:xs) n
    | otherwise = trouble (x:xs) n