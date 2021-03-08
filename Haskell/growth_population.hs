--- nlantau, 2021-03-08
-- NOT COMPLETED
-- Need to count the iterations some how. Or a different approach

module Codewars.G964.Arge where

nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p
    | ans > p = ans
    | otherwise = nbYear ans percent aug p
    where ans = floor (fromIntegral p0 + (fromIntegral p0 * percent * 0.01) + fromIntegral aug) :: Int
    

