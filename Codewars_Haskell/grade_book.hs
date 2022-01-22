-- nlantau, 2021-02-25

module GradeBook (getGrade) where

getGrade :: Double -> Double -> Double -> Char
getGrade x y z
    | ans >= 90 = 'A'
    | ans >= 80 = 'B'
    | ans >= 70 = 'C'
    | ans >= 60 = 'D'
    | ans >= 0 = 'F'
    where ans = (x + y + z) / 3
