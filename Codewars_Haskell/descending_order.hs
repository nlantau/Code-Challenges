-- nlantau, 2021-02-25

module DescendingOrder where
import Data.List

descendingOrder :: Integer -> Integer
descendingOrder a = read $ concat $ reverse $ sort $ map (:[]) (show a) 

{-
module DescendingOrder where

import Data.List
import Control.Category

descendingOrder :: Integer -> Integer
descendingOrder = show >>> sort >>> reverse >>> read

------------------

module DescendingOrder where

import Data.List (sort)

descendingOrder :: Integer -> Integer
descendingOrder = read . reverse . sort . show

-}