-- nlantau, 2021-03-03
-- Completed

module PowersOfTwo where

powersOfTwo :: Int -> [Int]
powersOfTwo n = [2^x | x <- [0..n]]


{-
module PowersOfTwo where
powersOfTwo :: Int -> [Int]
powersOfTwo = map (2 ^) . enumFromTo 0

module PowersOfTwo where
powersOfTwo :: Int -> [Int]
powersOfTwo n = map (2 ^) [0..n]

module PowersOfTwo where
powersOfTwo :: Int -> [Int]
powersOfTwo n = (2^) <$> [0..n]
-}