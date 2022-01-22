-- nlantau, 2021-03-04

module DivisibleBy (divisibleBy) where

divisibleBy :: [Int] -> Int -> [Int]
divisibleBy li a = filter (\i -> i `mod` a == 0) li

{-
module DivisibleBy (divisibleBy) where
divisibleBy :: [Int] -> Int -> [Int]
divisibleBy l n = filter ((== 0) . (`mod` n)) l

module DivisibleBy (divisibleBy) where
divisibleBy :: [Int] -> Int -> [Int]
divisibleBy xs num= [x | x<-xs, x `mod` num == 0]
-}