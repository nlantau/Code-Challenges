-- nlantau, 2021-03-03

module Haskell.Codewars.ParseNiceInt where
import Data.Char

getAge :: (Integral a, Read a) => String -> a
getAge x = read $ filter isDigit x

{-
module Haskell.Codewars.ParseNiceInt where
getAge :: (Integral a, Read a) => String -> a
getAge = read . take 1

module Haskell.Codewars.ParseNiceInt where
getAge :: (Integral a, Read a) => String -> a
getAge = read . head . words
-}