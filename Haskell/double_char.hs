-- nlantau, 2021-03-03

module Codewars.Strings where


doubleChar :: [Char] -> [Char]
doubleChar [] = []
doubleChar (x:xs) = x : x : doubleChar xs
