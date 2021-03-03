-- nlantau, 2021-03-03
-- Not completed. Some bs tests


module Welcome where

sayhello :: [String] -> String -> String -> String
sayhello [x,y] c s = "Hello, " ++ x ++ " " ++ y ++ "! " ++ "Welcome to " ++ c ++ ", " ++ s ++ "!"