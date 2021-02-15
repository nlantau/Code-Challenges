-- nlantau, 2020-02-15
-- Completed


import Data.List


uniqueInOrder :: Eq a => [a] -> [a]
uniqueInOrder = map head . group

{-

group: [AAAABBBCCDAABBB] -> [[AAAA], [BBB], [CC], [D], [AA], [BBB]]
map: head [[AAAA], [BBB], [CC], [D], [AA], [BBB]] -> [ABCDAB]

uniqueInOrder "AAAABBBCCDAABBB" == "ABCDAB"
uniqueInOrder "ABBCcAD"         == "ABCcAD"
uniqueInOrder [1,2,2,3,3]       == [1,2,3]


-}
