-- nlatau, 2021-02-25

module Kata.OddOrEven where

oddOrEven :: [Integer] -> String
oddOrEven a
    | mod ans 2 == 0 = "even"
    | otherwise = "odd"
    where ans = sum a