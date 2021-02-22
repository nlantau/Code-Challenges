-- nlantau, 2021-02-22
-- Completed

module Codewars.IsThisMyTail where

correctTail :: String -> Char -> Bool
correctTail x y = last x == y
--correctTail bod ta = if ta == last bod then True else False 