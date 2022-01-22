-- nlantau, 2021-03-08

module FindShortest where
import Data.List
import Data.Function

find_shortest :: String -> Integer
find_shortest = toInteger . length . head . sortBy (compare `on` length) . words

{- Clever Solutions::

module FindShortest where
find_shortest :: String -> Integer
find_shortest = fromIntegral.minimum.map length.words

module FindShortest where

import Data.List 
find_shortest :: String -> Integer
find_shortest = fromIntegral . minimum . map length . words 

module FindShortest where

import Data.List (minimumBy)
import Data.Ord (comparing)

find_shortest :: String -> Integer
find_shortest = toInteger . length . minimumBy (comparing length) . words

-}