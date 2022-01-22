-- nlantau, 2020-02-17

switchero :: String -> String
switchero [] = []
switchero (x:xs) = if x == 'a' then 'b':switchero xs else if 
    x == 'b' then 'a':switchero xs else x:switchero xs