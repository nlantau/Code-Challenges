--- nlantau, 2021-03-08
-- NOT COMPLETED
-- Need to count the iterations some how. Or a different approach

module Codewars.G964.Arge where

{-
nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p
    | ans > p = ans
    | otherwise = nbYear ans percent aug p
    where ans = floor (fromIntegral p0 + (fromIntegral p0 * percent * 0.01) + fromIntegral aug) :: Int
-}

cal :: Int -> Double -> Int -> Int -> Int
cal p0 percent aug p = 
    floor (fromIntegral p0 + (fromIntegral p0 * percent * 0.01) + fromIntegral aug) :: Int

nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p
    | ans > p = ans
    | otherwise = cal p0 percent aug ans
    where ans = cal p0 percent aug p
          li = [ans]


{- Clever Solutions::

module Codewars.G964.Arge where

nbYear :: Int -> Double -> Int -> Int -> Int
nbYear p0 percent aug p = nbYearAux p0 percent aug p 1
    where
        nbYearAux :: Int -> Double -> Int -> Int -> Int -> Int
        nbYearAux p0 percent aug p i
            | p0 >= p = i - 1
            | otherwise = nbYearAux (floor (fromIntegral p0 * mult + fromIntegral aug)) percent aug p (i + 1)
                where
                    mult = 1 + percent / 100.0




-}