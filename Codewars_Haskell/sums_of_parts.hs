--- nlantau, 2021-02-22
-- Passes the initial tests, but gets Execution Timed Out
-- when attempting. 
-- How can we solve this faster?


partsSum :: [Integer] -> [Integer]
partsSum [] = [0]
--partsSum lst@(x:xs) = sum lst : (foldr (+) 0 (partsSum xs))
partsSum lst@(x:xs) = sum lst : partsSum xs


{-
1. sum list
2. sum step 1 - first element
3. sum step 2 - first element
-}