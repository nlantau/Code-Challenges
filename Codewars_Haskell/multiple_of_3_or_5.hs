-- nlantau, 2021-02-16

solution :: Integer -> Integer
solution a = sum [ x | x <- [0..a-1], mod x 3 == 0 || mod x 5 == 0]