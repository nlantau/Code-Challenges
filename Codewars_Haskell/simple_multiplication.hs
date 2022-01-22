-- nlantau, 2021-03-04

module Codewars.MichM.SimpleMultiplication where

simpleMultiplication :: Int -> Int
simpleMultiplication n 
    | even n = n * 8
    | otherwise = n * 9