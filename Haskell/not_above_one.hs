-- nlantau, 2021-02-16

import Data.Maybe
import Data.List

{-
   My solution (that did not solve the problem (did not even compile))

binaryCleaner :: [Int] -> ([Int], [Int])
binaryCleaner xs = [ ([x],[y]) | x <- xs, y <- xs ]
-}

-- Stolen solutions:


binaryCleaner :: [Int] -> ([Int], [Int])
binaryCleaner x =
    let smaller = [ a | a <- x, a < 2 ]
        larger  = [ i | (i, v) <- zip [0..] x, v >= 2 ]
    in (smaller, larger)


t :: [Int] -> [Int]
t x = [ i | (i, v) <- zip [0..] x]
