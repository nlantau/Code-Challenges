-- nlantau, 2021-02-16
-- Completed

createList :: Int -> [Int]
createList n = takeWhile (<= n) [1..]
