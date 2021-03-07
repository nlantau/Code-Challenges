-- nlantau, 2021-03-04

import Data.List
import Data.Char

main :: IO()
main = 
    do
        name <- readFile "numbs.in"
        let names = map (read::String->Int) $ words name
        putStrLn . show $ names