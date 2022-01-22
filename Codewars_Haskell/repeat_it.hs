-- nlantau, 2021-03-03

module Codewars.Exercises.RepeatIt where

repeatIt :: String -> Int -> String
repeatIt str n = take (n * length str) (cycle str)