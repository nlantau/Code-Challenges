-- nlantau, 2021-02-25

findDifference :: (Int, Int, Int) -> (Int, Int, Int) -> Int
findDifference (x,y,z) (a,b,c)
    | (x*y*z) > (a*b*c) = (x*y*z) - (a*b*c)
    | (x*y*z) <= (a*b*c) = (a*b*c) - (x*y*z)

