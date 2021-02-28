-- nlantau, 2021-02-26

module Codewars.Kata.Count where

countBy :: Int -> Int -> [Int]
countBy x n = [y * x | y <- [1..(x*n)]]

{-
x n  -> lst
1 10 -> [1,2,3,4,5,6,7,8,9,10] 
1 5  -> [1,2,3,4,5]
2 5  -> [2,4,6,8,10]
3 6  -> [3,6,9,12,15,18]

=> x * n = value of last element

----------------------> Clever solutions

module Codewars.Kata.Count where

countBy :: Integer -> Int -> [Integer]
countBy x n = take n [x, x + x..]

module Codewars.Kata.Count where

countBy :: Integer -> Integer -> [Integer]
countBy x n = map (*x) [1..n]


-}