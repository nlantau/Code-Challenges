-- nlantau, 2021-03-04

{- # TODO: Not done # -} 

module Codewars.Kata.TenMinuteWalk where
import Data.Char
import Data.List
import Data.Function

-- isValidWalk :: [Char] -> Bool
--isValidWalk x = reverse $ sortBy (on compare length) $ group $ sort x
isValidWalk x = group $ sort x