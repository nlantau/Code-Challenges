-- nlantau, 2021-02-14
-- Completed

remove :: String -> String
remove str = if last str == '!' then init str else str

-- ...series_num2
removeAllExlamationmarks :: String -> String
removeAllExlamationmarks str = if last str == '!' then removeAllExlamationmarks $ init str else str

-- using guards
removeAllExlamationmarks2 :: String -> String
removeAllExlamationmarks2 str
    | last str == '!' = removeAllExlamationmarks2 $ init str
    | otherwise = str
