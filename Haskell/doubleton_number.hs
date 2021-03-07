-- nlantau, 2021-03-07
-- Actually quite satisfied with this one!


module DoubletonNumber (doubleton) where
import Data.List
import Data.Char

doubleton :: Int -> Int
doubleton x
    | isDt x == 2 = getNextDt x
    | otherwise = getNextDt x

isDt :: Int -> Int
isDt = length . group . sort . show

getNextDt :: Int -> Int
getNextDt x = if isDt (x + 1) == 2 then x + 1 else getNextDt (x + 1)

{-
{-# Language ViewPatterns #-}
module DoubletonNumber (doubleton) where
import Data.Set (fromList)
doubleton :: Int -> Int
doubleton (succ -> n) | isDoubleton n = n
                      | otherwise = doubleton n
                      where isDoubleton = (== 2) . length . fromList . show




-}