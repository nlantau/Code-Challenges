-- nlantau, 2021-03-04

module Codwars.Kata.Duplicates where
import Data.Char
import Data.List

duplicateCount :: String -> Int
duplicateCount x = length $ filter ((> 1) . length) $ group $ sort $ map toLower x


{-
module Codwars.Kata.Duplicates where
import Data.Char
import Data.List

duplicateCount :: String -> Int
duplicateCount = length . filter ((> 1) . length) . group . sort . map toLower




-}