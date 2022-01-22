-- nlantau, 2021-02-13
-- Complete the function which converts hex number (given as string) to a decimal number
-- Stolen solution

hexCharToInt :: Char -> Int
hexCharToInt c
    | c == '0' = 0
    | c == '1' = 1
    | c == '2' = 2
    | c == '3' = 3
    | c == '4' = 4
    | c == '5' = 5
    | c == '6' = 6
    | c == '7' = 7
    | c == '8' = 8
    | c == '9' = 9
    | c == 'a' = 10
    | c == 'b' = 11
    | c == 'c' = 12
    | c == 'd' = 13
    | c == 'e' = 14
    | c == 'f' = 15
    | otherwise = 0


hexToDec :: String -> Int
hexToDec hxS
    | length hxS /= 0 = hexCharToInt (last hxS) + 16 * hexToDec (init hxS)
    | otherwise = 0


{-
    Clever solutions / Need to learn this

    hexToDec :: String -> Int
    hexToDec = read . ("0x" ++)

-}

ht :: String -> Int
ht = read . ("0x" ++)



