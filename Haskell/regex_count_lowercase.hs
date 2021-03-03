-- nlantau, 2021-03-03

module Codewars.Strings where
import Data.Char

lowercaseCount :: [Char] -> Int
lowercaseCount = length . filter isLower
