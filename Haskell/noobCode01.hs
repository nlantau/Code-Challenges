-- nlantau, 2021-03-03
-- Completed


module Codewars.Kata.Supersize where
import Data.List(sort)

superSize :: Integer -> Integer
superSize = read . reverse . sort . show