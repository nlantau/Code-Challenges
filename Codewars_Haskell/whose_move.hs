-- nlantau, 2021-02-27

module Kata.WhoseMove (whoseMove) where

whoseMove :: String -> Bool -> String
whoseMove lp w
    | lp == "black" && w == True = "black"
    | lp == "black" && w == False = "white"
    | lp == "white" && w == True = "white"
    | otherwise = "black"
