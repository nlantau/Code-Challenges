-- nlantau, 2021-02-20
-- Completed
import Data.Char

isUpperCase :: String -> Bool
isUpperCase [x] = isUpper x || not (isAlpha x)
isUpperCase (x:xs) = if isUpper x || not (isAlpha x) then isUpperCase xs else False

-- Clever solutions by others
{-

import Data.Char (isLower)
isUpperCase :: String -> Bool
isUpperCase = not . any isLower


import Data.Char
isUpperCase :: String -> Bool
isUpperCase = null.filter (isLower)


import Data.Char (toUpper)
isUpperCase :: String -> Bool
isUpperCase = (==) <*> (map toUpper)


import Data.Char
isUpperCase :: String -> Bool
isUpperCase str = 
  all isUpper (filter isAlpha str)


import Data.Char
isUpperCase :: String -> Bool
isUpperCase str = not (any isLower str)

import Data.Char
isUpperCase :: String -> Bool
isUpperCase s = foldr (&&) True (map (\x -> isUpper x || not (isLetter x) ) s)


import Data.Char (isLower)
isUpperCase :: String -> Bool
isUpperCase = all (not . isLower)

-}
