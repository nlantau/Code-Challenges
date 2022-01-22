-- nlantau, 2021-02-20
-- Completed


whoIsPaying :: String -> [String]
--whoIsPaying "" = [""]
whoIsPaying n = if length n <= 2 then [n] else [n, take 2 n]
