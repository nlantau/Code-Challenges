-- nlantau, 2021-03-03


module Codewars.Kata.Square where

isSquare :: Integral n => n -> Bool
isSquare n = n == (floor $ sqrt n)